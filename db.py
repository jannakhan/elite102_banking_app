import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL DEFAULT 0.0
)
""")
conn.commit()


def create_account(name, deposit_amount):
    cursor.execute(
        "INSERT INTO accounts (name, balance) VALUES (?, ?)",
        (name, deposit_amount)
    )
    conn.commit()
    return "Account created successfully."


def deposit_money(name, amount):
    cursor.execute("SELECT balance FROM accounts WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        new_balance = result[0] + amount
        cursor.execute(
            "UPDATE accounts SET balance = ? WHERE name = ?",
            (new_balance, name)
        )
        conn.commit()
        return "Deposit successful."
    return "Account not found."


def withdraw_money(name, amount):
    cursor.execute("SELECT balance FROM accounts WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        if result[0] >= amount:
            new_balance = result[0] - amount
            cursor.execute(
                "UPDATE accounts SET balance = ? WHERE name = ?",
                (new_balance, name)
            )
            conn.commit()
            return "Withdrawal successful."
        return "Insufficient funds."
    return "Account not found."


def check_balance(name):
    cursor.execute("SELECT balance FROM accounts WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        return f"Balance: ${result[0]:.2f}"
    return "Account not found."