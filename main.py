import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Ошибка", "Введите задачу!")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Ошибка", "Выберите задачу для удаления!")

# Создаем главное окно
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Ввод задачи
task_entry = tk.Entry(root, width=25)
task_entry.pack(pady=10)

# Кнопки
add_button = tk.Button(root, text="Добавить задачу", width=20, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", width=20, command=delete_task)
delete_button.pack(pady=5)

# Список задач
tasks_listbox = tk.Listbox(root, width=40, height=15)
tasks_listbox.pack(pady=10)

# Запуск приложения
root.mainloop()
