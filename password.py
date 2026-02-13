import tkinter as tk
from tkinter import messagebox
import secrets
import string


def generate_password():
    try:
        length = int(length_box.get())

        if length <= 0:
            messagebox.showwarning("Warning", "Length should be greater than 0")
            return

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""
        for i in range(length):
            ch = secrets.choice(characters)
            password = password + ch

        output_box.config(state="normal")
        output_box.delete(0, tk.END)
        output_box.insert(0, password)
        output_box.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Enter numbers only")


def copy_password():
    text = output_box.get()

    if text == "":
        messagebox.showwarning("Warning", "Please generate password first")
    else:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Password copied")


root = tk.Tk()
root.title("Password Generator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#e6f2ff")

tk.Label(root, text="Enter Password Length", font=("Arial", 11), bg="#e6f2ff", fg="#003366").pack(pady=15)

length_box = tk.Entry(root, width=12, justify="center", bg="white")
length_box.insert(0, "12")
length_box.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password, bg="#4da6ff", fg="white", width=16).pack(pady=12)

output_box = tk.Entry(root, width=26, font=("Courier", 12), justify="center", state="readonly", bg="white")
output_box.pack(pady=10)

tk.Button(root, text="Copy Password", command=copy_password, bg="#66cc66", fg="white", width=16).pack(pady=8)

root.mainloop()
