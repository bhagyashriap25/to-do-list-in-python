import sqlite3
from datetime import datetime

DB_NAME = 'tasks.db'

def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT CHECK(priority IN ('high', 'medium', 'low')) NOT NULL DEFAULT 'medium',
            due_date TEXT,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_task(title, description, priority, due_date):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO tasks (title, description, priority, due_date, completed)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, description, priority, due_date, False))
    conn.commit()
    conn.close()

def remove_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def mark_task_completed(task_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def list_tasks():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return tasks

def main():
    initialize_db()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            title = input("Title: ")
            description = input("Description: ")
            priority = input("Priority (high, medium, low): ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            add_task(title, description, priority, due_date)
        elif choice == '2':
            task_id = int(input("Task ID to remove: "))
            remove_task(task_id)
        elif choice == '3':
            task_id = int(input("Task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == '4':
            tasks = list_tasks()
            for task in tasks:
                print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}, Priority: {task[3]}, Due Date: {task[4]}, Completed: {task[5]}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
