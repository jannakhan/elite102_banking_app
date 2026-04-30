import tkinter as tk
from tkinter import messagebox
from db import create_account, deposit_money, withdraw_money, check_balance


root = tk.Tk()
root.title("Banking App")
root.geometry("400x350")
root.config(bg="#dbeafe")


# Labels + inputs
tk.Label(root, text="Banking App", font=("Arial", 18, "bold"), bg="#dbeafe").pack(pady=10)

tk.Label(root, text="Name:", bg="#dbeafe").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Amount:", bg="#dbeafe").pack()
amount_entry = tk.Entry(root, width=30)
amount_entry.pack(pady=5)


def get_inputs():
    name = name_entry.get()
    amount = amount_entry.get()

    try:
        amount = float(amount) if amount else 0
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")
        return None, None

    return name, amount


def create():
    name, amount = get_inputs()
    if name:
        result = create_account(name, amount)
        messagebox.showinfo("Success", result)


def deposit():
    name, amount = get_inputs()
    if name:
        result = deposit_money(name, amount)
        messagebox.showinfo("Result", result)


def withdraw():
    name, amount = get_inputs()
    if name:
        result = withdraw_money(name, amount)
        messagebox.showinfo("Result", result)


def balance():
    name = name_entry.get()
    result = check_balance(name)
    messagebox.showinfo("Balance", result)


# Buttons
tk.Button(root, text="Create Account", width=20, command=create).pack(pady=5)
tk.Button(root, text="Deposit", width=20, command=deposit).pack(pady=5)
tk.Button(root, text="Withdraw", width=20, command=withdraw).pack(pady=5)
tk.Button(root, text="Check Balance", width=20, command=balance).pack(pady=5)

root.mainloop()