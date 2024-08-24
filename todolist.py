import tkinter as tk
from tkinter import messagebox


r = tk.Tk()
r.title("To-Do List Application")
r.configure(bg="black")
r.option_add('*foreground', 'white')


tasks = []

def add_task():
    task_name = task_entry.get()
    if task_name:
        tasks.append(task_name)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def update_listbox():
    tasks_listbox.delete(0, tk.END)
    
    
    for task in tasks:
        tasks_listbox.insert(tk.END, task)


def remove_task():
    try:
        index = tasks_listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")


task_label = tk.Label(r, text="Enter Task:",bg='black')
task_label.pack(pady=10)

task_entry = tk.Entry(r, width=50,bg='black')
task_entry.pack()

add_button = tk.Button(r, text="Add Task", command=add_task,bg = 'black',fg="white")
add_button.pack(pady=10)

remove_button = tk.Button(r, text="Remove Task", command=remove_task,bg='black',fg="white")
remove_button.pack()

tasks_listbox = tk.Listbox(r, height=10, width=50,bg='black',fg='white')
tasks_listbox.pack(padx=10, pady=10)


r.mainloop()
