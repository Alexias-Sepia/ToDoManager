import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "tasks.json"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.frame, text="Добавить", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Удалить выбранное", command=self.delete_task)
        self.delete_button.pack()

        self.load_tasks()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Предупреждение", "Введите задачу!")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.listbox.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("Предупреждение", "Выберите задачу для удаления!")

    def load_tasks(self):
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r", encoding="utf-8") as file:
                    self.tasks = json.load(file)
                    for task in self.tasks:
                        self.listbox.insert(tk.END, task)
            except (json.JSONDecodeError, IOError):
                messagebox.showerror("Ошибка", "Не удалось загрузить список задач.")

    def save_tasks(self):
        try:
            with open(FILENAME, "w", encoding="utf-8") as file:
                json.dump(self.tasks, file, ensure_ascii=False, indent=4)
        except IOError:
            messagebox.showerror("Ошибка", "Не удалось сохранить список задач.")

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()