import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List

DATA_FILE = Path(__file__).with_suffix('.json')

@dataclass
class Task:
    id: int
    text: str
    done: bool = False


def load_tasks() -> List[Task]:
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open('r', encoding='utf-8') as f:
            data = json.load(f)
        return [Task(**item) for item in data]
    except (json.JSONDecodeError, TypeError):
        return []


def save_tasks(tasks: List[Task]) -> None:
    with DATA_FILE.open('w', encoding='utf-8') as f:
        json.dump([asdict(task) for task in tasks], f, ensure_ascii=False, indent=2)


def list_tasks(tasks: List[Task]) -> None:
    if not tasks:
        print('Žádné úkoly v seznamu.')
        return
    print('\nTvůj To-do list:')
    for task in tasks:
        status = '✔' if task.done else '✗'
        print(f'{task.id}. [{status}] {task.text}')
    print()


def add_task(tasks: List[Task], text: str) -> None:
    task_id = max((task.id for task in tasks), default=0) + 1
    tasks.append(Task(id=task_id, text=text))
    save_tasks(tasks)
    print(f'Přidáno: {task_id}. {text}')


def complete_task(tasks: List[Task], task_id: int) -> None:
    for task in tasks:
        if task.id == task_id:
            task.done = True
            save_tasks(tasks)
            print(f'Úkol označen jako hotový: {task.id}. {task.text}')
            return
    print(f'Úkol s ID {task_id} nebyl nalezen.')


def delete_task(tasks: List[Task], task_id: int) -> None:
    for i, task in enumerate(tasks):
        if task.id == task_id:
            removed = tasks.pop(i)
            save_tasks(tasks)
            print(f'Odstraněno: {removed.id}. {removed.text}')
            return
    print(f'Úkol s ID {task_id} nebyl nalezen.')


def clear_tasks(tasks: List[Task]) -> None:
    confirm = input('Opravdu chcete smazat všechny úkoly? (ano/ne): ').strip().lower()
    if confirm in {'ano', 'a', 'yes', 'y'}:
        tasks.clear()
        save_tasks(tasks)
        print('Všechny úkoly byly smazány.')
    else:
        print('Akce zrušena.')


def interactive_menu() -> None:
    tasks = load_tasks()
    while True:
        print('\n=== To-do list CLI ===')
        print('1) Seznam úkolů')
        print('2) Přidat úkol')
        print('3) Označit úkol jako hotový')
        print('4) Odstranit úkol')
        print('5) Smazat všechny úkoly')
        print('0) Konec')
        choice = input('Vyber volbu: ').strip()

        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            text = input('Zadej popis úkolu: ').strip()
            if text:
                add_task(tasks, text)
            else:
                print('Popis nesmí být prázdný.')
        elif choice == '3':
            try:
                task_id = int(input('ID úkolu ke označení: ').strip())
                complete_task(tasks, task_id)
            except ValueError:
                print('Zadej platné číselné ID.')
        elif choice == '4':
            try:
                task_id = int(input('ID úkolu k odstranění: ').strip())
                delete_task(tasks, task_id)
            except ValueError:
                print('Zadej platné číselné ID.')
        elif choice == '5':
            clear_tasks(tasks)
        elif choice == '0':
            print('Na shledanou!')
            break
        else:
            print('Neplatná volba. Zkus to znovu.')


def main() -> None:
    parser = argparse.ArgumentParser(description='Jednoduchý To-do list CLI')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('list', help='Zobrazit všechny úkoly')

    add_parser = subparsers.add_parser('add', help='Přidat nový úkol')
    add_parser.add_argument('text', nargs='+', help='Text úkolu')

    done_parser = subparsers.add_parser('done', help='Označit úkol jako hotový')
    done_parser.add_argument('id', type=int, help='ID úkolu')

    delete_parser = subparsers.add_parser('delete', help='Odstranit úkol')
    delete_parser.add_argument('id', type=int, help='ID úkolu')

    subparsers.add_parser('clear', help='Smazat všechny úkoly')

    args = parser.parse_args()
    tasks = load_tasks()

    if args.command == 'list':
        list_tasks(tasks)
    elif args.command == 'add':
        add_task(tasks, ' '.join(args.text))
    elif args.command == 'done':
        complete_task(tasks, args.id)
    elif args.command == 'delete':
        delete_task(tasks, args.id)
    elif args.command == 'clear':
        clear_tasks(tasks)
    else:
        interactive_menu()


if __name__ == '__main__':
    main()
