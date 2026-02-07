import tkinter as tk
from tkinter import messagebox
import os

file = "tasks.txt"


def load():
    data = []
    if os.path.exists(file):
        f = open(file, "r")
        lines = f.readlines()
        for i in lines:
            data.append(i.strip())
        f.close()
    return data


def save():
    f = open(file, "w")
    for i in tasks:
        f.write(i + "\n")
    f.close()


def add():
    t = box.get()
    if t == "":
        messagebox.showwarning("Warning", "write something")
        return
    tasks.append(t)
    show()
    box.delete(0, tk.END)
    save()


def done():
    try:
        i = listbox.curselection()[0]
        if not tasks[i].startswith("done "):
            tasks[i] = "done:-" + tasks[i]
        show()
        save()
    except:
        messagebox.showwarning("Warning", "select task")


def delete():
    try:
        i = listbox.curselection()[0]
        tasks.pop(i)
        show()
        save()
    except:
        messagebox.showwarning("Warning", "select task")


def show():
    listbox.delete(0, tk.END)
    for i in tasks:
        listbox.insert(tk.END, i)


root = tk.Tk()
root.title("todo")
root.geometry("400x500")
root.configure(bg="#d0f0ff")

label = tk.Label(root, text="To-Do list", font=("Arial", 16), bg="#d0f0ff", fg="black")
label.pack(pady=10)

box = tk.Entry(root, bg="white", fg="black")
box.pack(pady=10)

btn1 = tk.Button(root, text="Add", command=add, bg="#4CAF50", fg="white", width=15)
btn1.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=12, bg="#fffacd", fg="black")
listbox.pack(pady=10)

frame = tk.Frame(root, bg="#d0f0ff")
frame.pack()

btn2 = tk.Button(frame, text="Done", command=done, bg="#2196F3", fg="white", width=10)
btn2.pack(side=tk.LEFT, padx=5)

btn3 = tk.Button(frame, text="Delete", command=delete, bg="#f44336", fg="white", width=10)
btn3.pack(side=tk.LEFT, padx=5)

tasks = load()
show()

root.mainloop()
