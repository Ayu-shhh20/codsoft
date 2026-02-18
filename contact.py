import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Enter Name and Phone")
        return

    contacts.append([name, phone])
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    view_contacts()

def view_contacts():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, contact[0] + " - " + contact[1])

def search_contact():
    name = name_entry.get()
    listbox.delete(0, tk.END)

    found = False
    for contact in contacts:
        if name.lower() in contact[0].lower():
            listbox.insert(tk.END, contact[0] + " - " + contact[1])
            found = True

    if not found:
        messagebox.showinfo("Result", "Contact Not Found")

def delete_contact():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select contact to delete")
        return

    index = selected[0]
    del contacts[index]
    view_contacts()

root = tk.Tk()
root.title("Contact Book by Ayush")
root.geometry("350x450")

tk.Label(root, text="Contact Book", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame, width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Phone").grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(frame, width=25)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=12, command=add_contact).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Search", width=12, command=search_contact).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Delete", width=12, command=delete_contact).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="View All", width=12, command=view_contacts).grid(row=1, column=1, padx=5, pady=5)

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=40, height=12, yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

root.mainloop()
