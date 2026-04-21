import sqlite3

# Connect to a persistent database file (NOT in-memory)
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create tables (only runs once if they don’t exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL DEFAULT 0.0
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER,
    type TEXT,
    amount REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
)
''')

conn.commit()

#functions

def create_account():
    name = input("Enter your name: ")
    deposit_amount = float(input("Initial deposit: "))
    
    cursor.execute(
        "INSERT INTO accounts (name, balance) VALUES (?, ?)",
        (name, deposit_amount)
    )
    conn.commit()
    
    print("Account created!\n")

def deposit():
    name = input("Enter your name: ")
    amount = float(input("Deposit amount: "))
    
    cursor.execute("SELECT balance FROM accounts WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        new_balance = result[0] + amount
        cursor.execute(
            "UPDATE accounts SET balance = ? WHERE name = ?",
            (new_balance, name)
        )
        conn.commit()
        print("Deposit successful!\n")
    else:
        print("Account not found.\n")


def withdraw():
    name = input("Enter your name: ")
    amount = float(input("Withdraw amount: "))
    
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
            print("Withdrawal successful!\n")
        else:
            print("Not enough money.\n")
    else:
        print("Account not found.\n")


def check_balance():
    name = input("Enter your name: ")
    
    cursor.execute("SELECT balance FROM accounts WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        print(f"Balance: ${result[0]}\n")
    else:
        print("Account not found.\n")