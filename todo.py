import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set the background color and window size
root.configure(bg="#D7E5CA")
root.geometry("400x400")

# Create a heading label
heading_label = tk.Label(root, text="To-Do List", font=("Arial", 20), bg="#D7E5CA")
heading_label.pack(pady=10)

# Create an input field
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

# Create a button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12))
add_button.pack(pady=10)

# Create a listbox to display tasks
listbox = tk.Listbox(root, width=30, height=10, font=("Arial", 12))
listbox.pack()

# Create a button to delete selected task
delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=("Arial", 12))
delete_button.pack(pady=10)

root.mainloop()
