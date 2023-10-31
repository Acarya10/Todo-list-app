import tkinter as tk
import pickle
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []
        self.load_tasks()
        
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)
        
        view_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        view_button.pack(pady=5)
        
        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5)
        
        save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        save_button.pack(pady=5)
        
        load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        load_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)

    def view_tasks(self):
        if self.tasks:
            tasks_text = "\n".join(self.tasks)
            messagebox.showinfo("Tasks", tasks_text)
        else:
            messagebox.showinfo("Tasks", "No tasks available.")

    def delete_task(self):
        task = self.task_entry.get()
        if task in self.tasks:
            self.tasks.remove(task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Task not found", "Task not found in the list.")

    def save_tasks(self):
        with open("tasks.pkl", "wb") as file:
            pickle.dump(self.tasks, file)
        messagebox.showinfo("Tasks Saved", "Tasks have been saved to tasks.pkl")

    def load_tasks(self):
        try:
            with open("tasks.pkl", "rb") as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            self.tasks = []
        messagebox.showinfo("Tasks Loaded", "Tasks have been loaded from tasks.pkl")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
