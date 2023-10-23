"""
Author: Akash Chaudhary
GitHub Handle: akashchaudhary-git

This script allows users to add tasks, view tasks, and delete tasks from the list.
"""

import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Create and configure the listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Create and configure the entry for adding new tasks
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create and configure the buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Run the main event loop
root.mainloop()
