import sqlite3

conn = sqlite3.connect("bank.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    balance REAL
)
""")
conn.commit()


def create_account(name, amount):
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, amount))
    conn.commit()
    return "Account created"


def deposit(name, amount):
    cursor.execute("SELECT balance FROM accounts WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        new_balance = result[0] + amount
        cursor.execute("UPDATE accounts SET balance = ? WHERE name = ?", (new_balance, name))
        conn.commit()
        return "Deposit successful"
    return "Account not found"


def withdraw(name, amount):
    cursor.execute("SELECT balance FROM accounts WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        if result[0] >= amount:
            new_balance = result[0] - amount
            cursor.execute("UPDATE accounts SET balance = ? WHERE name = ?", (new_balance, name))
            conn.commit()
            return "Withdraw successful"
        return "Not enough money"
    return "Account not found"


def check_balance(name):
    cursor.execute("SELECT balance FROM accounts WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        balance = result[0]
        message = "Balance: $" + str(balance)
        return message
    else:
        return "Account not found"