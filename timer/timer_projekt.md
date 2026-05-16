# Pomodoro Timer

Simple Pomodoro timer with a minimal `Tkinter` GUI. Features:

- Start work / start break / pause / reset
- Persist completed sessions to `sessions.json`

Run:

```bash
python pomodoro.py
```

Run unit tests:

```bash
python -m unittest discover -s pomodoro -p "test_*.py"
```

Notes:
- The GUI requires a desktop environment to run (`tkinter` must be available).
- Sessions are appended to `sessions.json` when a session completes.

