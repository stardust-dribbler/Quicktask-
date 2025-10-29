import json, os, sys

DATA_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(task):
    tasks = load_tasks()
    tasks.append({'task': task, 'done': False})
    save_tasks(tasks)
    print(f'✅ Added: {task}')

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print('📭 No tasks found.')
        return
    for i, t in enumerate(tasks, 1):
        status = '✅' if t['done'] else '❌'
        print(f'{i}. {t["task"]} [{status}]')

def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index-1]['done'] = True
        save_tasks(tasks)
        print(f'🎯 Task {index} marked as done.')
    else:
        print('⚠️ Invalid task number.')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python src/main.py [add|list|done] <task>')
        sys.exit(1)

    command = sys.argv[1]
    if command == 'add' and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif command == 'list':
        list_tasks()
    elif command == 'done' and len(sys.argv) > 2:
        mark_done(int(sys.argv[2]))
    else:
        print('Invalid command.')
