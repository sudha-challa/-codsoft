import tkinter as tk
import pyperclip
import random
def copyclipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)
def low():
    length = passlen.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password
    elif var.get() == 2:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password

def generate():
    password1 = low()
    passwrd.set(password1)
root = tk.Tk()
root.geometry("700x300")

passwrd = tk.StringVar()
passlen = tk.IntVar()
passlen.set(0)
root.title("Password Generator")

tk.Label(root, text="Strong Password Generator", font="Courier 30 bold").grid(row=0, column=0, columnspan=2)
tk.Label(root, text="Enter the number to get password").grid(row=1, column=0, sticky="w")
tk.Entry(root, textvariable=passlen).grid(row=1, column=1, sticky="w")

var = tk.IntVar()
var.set(1)  # Set a default value for var

tk.Radiobutton(root, text="Lowercase", variable=var, value=1).grid(row=2, column=0, sticky="w")
tk.Radiobutton(root, text="Uppercase", variable=var, value=2).grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Mixed", variable=var, value=3).grid(row=2, column=2, sticky="w")

tk.Button(root, text="Tap to get", command=generate).grid(row=3, column=0, columnspan=3, pady=7)
tk.Entry(root, textvariable=passwrd).grid(row=4, column=0, columnspan=2, sticky="w")
tk.Button(root, text="Tap to copy clipboard", command=copyclipboard).grid(row=4, column=2, sticky="w")
root.mainloop()
