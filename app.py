from flask import Flask, render_template, request, redirect, url_for
from db import create_account, deposit, withdraw, check_balance

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form.get("name")
        amount = request.form.get("amount")

        if amount:
            amount = float(amount)

        action = request.form.get("action")

        if action == "create":
            message = create_account(name, amount)
        elif action == "deposit":
            message = deposit(name, amount)
        elif action == "withdraw":
            message = withdraw(name, amount)
        elif action == "balance":
            message = check_balance(name)

        # 🔥 THIS FIXES THE POPUP ISSUE
        return redirect(url_for("home", message=message))

    message = request.args.get("message", "")
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)