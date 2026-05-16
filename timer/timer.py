import json
import os
import time
import threading
import datetime
try:
    import tkinter as tk
    from tkinter import messagebox
except Exception:
    # Pokud tkinter není dostupný (např. spuštění na headless serveru),
    # nastavíme `tk` na None a GUI části budou bezpečně ošetřeny.
    tk = None

# Cesta k souboru, kam se ukládají dokončené pomodoro seance.
SESSIONS_PATH = os.path.join(os.path.dirname(__file__), 'sessions.json')


class Timer:
    """Logika odpočítávacího časovače pro pomodoro.

    - `work_duration` a `break_duration` jsou v sekundách.
    - `state` může být: 'idle', 'work', 'break', 'paused'.
    - `_tick_callback` je volitelná funkce, která se zavolá pokaždé,
      když uběhne jedna sekunda (pro aktualizaci GUI apod.).
    """

    def __init__(self, work_minutes=25, break_minutes=5):
        # Převeď minuty na sekundy
        self.work_duration = int(work_minutes * 60)
        self.break_duration = int(break_minutes * 60)
        # `remaining` drží zbývající sekundy aktuální seance
        self.remaining = self.work_duration
        # Počáteční stav
        self.state = 'idle'  # idle, work, break, paused
        self._tick_callback = None

    def set_tick_callback(self, cb):
        # Nastaví callback, který přijímá jeden parametr: zbývající sekundy
        self._tick_callback = cb

    def start_work(self):
        # Spustí pracovní seanci (nastaví zbývající čas)
        self.state = 'work'
        self.remaining = self.work_duration

    def start_break(self):
        # Spustí pauzu
        self.state = 'break'
        self.remaining = self.break_duration

    def pause(self):
        # Pozastaví aktuální seanci
        if self.state in ('work', 'break'):
            self.state = 'paused'

    def resume(self):
        # Obnoví po pozastavení. Rozhodnutí, zda obnovit work/break,
        # je založeno na porovnání `remaining` s work_duration.
        if self.state == 'paused':
            self.state = 'work' if self.remaining <= self.work_duration else 'break'

    def reset(self):
        # Vrátí časovač do původního (idle) stavu
        self.state = 'idle'
        self.remaining = self.work_duration

    def tick(self, seconds=1):
        """Sníží `remaining` o `seconds`. Pokud seance dokončí,
        zavolá `_on_complete` a vrátí True.
        """
        if self.state not in ('work', 'break'):
            return False
        self.remaining -= seconds
        # Zavolej GUI callback (pokud existuje) pro aktualizaci zobrazení
        if self._tick_callback:
            try:
                self._tick_callback(self.remaining)
            except Exception:
                # Ignorujeme chyby callbacku, hlavní logika běží dál
                pass
        if self.remaining <= 0:
            completed_type = self.state
            self._on_complete(completed_type)
            return True
        return False

    def _on_complete(self, completed_type):
        # Při dokončení seance uložíme záznam do `sessions.json`.
        save_session({'type': completed_type, 'timestamp': datetime.datetime.now().isoformat(), 'duration': self.work_duration if completed_type == 'work' else self.break_duration})


def save_session(record):
    data = []
    try:
        if os.path.exists(SESSIONS_PATH):
            with open(SESSIONS_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
    except Exception:
        data = []
    data.append(record)
    try:
        with open(SESSIONS_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        pass


def format_time(sec: int) -> str:
    sec = max(0, int(sec))
    m, s = divmod(sec, 60)
    return f"{m:02d}:{s:02d}"


def run_gui():
    if tk is None:
        print('Tkinter not available in this environment.')
        return

    root = tk.Tk()
    root.title('Pomodoro Timer')
    timer = Timer(25, 5)

    label = tk.Label(root, text=format_time(timer.remaining), font=('Helvetica', 48))
    label.pack(padx=20, pady=10)

    status = tk.Label(root, text='Idle')
    status.pack()

    def update_label(rem):
        label.config(text=format_time(rem))

    timer.set_tick_callback(lambda r: root.after(0, update_label, r))
    running = {'val': False}

    def worker_loop():
        while running['val']:
            time.sleep(1)
            finished = timer.tick(1)
            if finished:
                root.after(0, lambda: messagebox.showinfo('Pomodoro', 'Session complete'))
                if timer.state == 'work':
                    timer.start_break()
                    root.after(0, lambda: status.config(text='Break'))
                else:
                    timer.start_work()
                    root.after(0, lambda: status.config(text='Work'))

    def start_work():
        timer.start_work()
        status.config(text='Work')
        running['val'] = True
        threading.Thread(target=worker_loop, daemon=True).start()

    def start_break_cmd():
        timer.start_break()
        status.config(text='Break')
        running['val'] = True
        threading.Thread(target=worker_loop, daemon=True).start()

    def pause_cmd():
        timer.pause()
        running['val'] = False
        status.config(text='Paused')

    def reset_cmd():
        timer.reset()
        label.config(text=format_time(timer.remaining))
        status.config(text='Idle')
        running['val'] = False

    frame = tk.Frame(root)
    frame.pack(pady=10)

    b1 = tk.Button(frame, text='Start Work', command=start_work)
    b1.grid(row=0, column=0, padx=5)
    b2 = tk.Button(frame, text='Start Break', command=start_break_cmd)
    b2.grid(row=0, column=1, padx=5)
    b3 = tk.Button(frame, text='Pause', command=pause_cmd)
    b3.grid(row=0, column=2, padx=5)
    b4 = tk.Button(frame, text='Reset', command=reset_cmd)
    b4.grid(row=0, column=3, padx=5)

    config_frame = tk.Frame(root)
    config_frame.pack(pady=6)

    tk.Label(config_frame, text='Work (min):').grid(row=0, column=0)
    work_var = tk.IntVar(value=25)
    work_spin = tk.Spinbox(config_frame, from_=1, to=180, width=5, textvariable=work_var)
    work_spin.grid(row=0, column=1, padx=4)

    tk.Label(config_frame, text='Break (min):').grid(row=0, column=2)
    break_var = tk.IntVar(value=5)
    break_spin = tk.Spinbox(config_frame, from_=1, to=60, width=5, textvariable=break_var)
    break_spin.grid(row=0, column=3, padx=4)

    def set_durations():
        try:
            w = int(work_var.get())
            b = int(break_var.get())
            if w <= 0 or b <= 0:
                raise ValueError()
        except Exception:
            messagebox.showerror('Invalid input', 'Please enter positive integer minutes for durations.')
            return
        timer.work_duration = int(w * 60)
        timer.break_duration = int(b * 60)
        if timer.state in ('idle', 'paused'):
            timer.remaining = timer.work_duration
            label.config(text=format_time(timer.remaining))
        messagebox.showinfo('Durations set', f'Work={w} min, Break={b} min')

    set_btn = tk.Button(root, text='Set Durations', command=set_durations)
    set_btn.pack(pady=4)

    root.mainloop()


if __name__ == '__main__':
    run_gui()
