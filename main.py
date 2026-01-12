import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

from budget import Budget, Expense
from calculations import calculateNewBalance
from storage import saveBudgetToFile, loadBudgetFromFile

# ======================
# App Setup
# ======================

budget = loadBudgetFromFile() or Budget(1500)

root = tk.Tk()
root.title("Budget Maker")
root.geometry("500x420")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

# ======================
# Header
# ======================

header = ttk.Label(
    root,
    text="Shared Budget Overview",
    font=("Segoe UI", 16, "bold")
)
header.pack(pady=(15, 5))

# ======================
# Summary Card
# ======================

summary_frame = ttk.Frame(root, padding=15)
summary_frame.pack(fill="x", padx=20, pady=10)

summary_label = ttk.Label(summary_frame, font=("Segoe UI", 12))
summary_label.pack()

def update_summary():
    summary_label.config(
        text=(
            f"💸 Spent: ${budget.totalSpent():.2f}\n"
            f"💰 Remaining: ${budget.remainingBudget():.2f}"
        )
    )

update_summary()

# ======================
# Buttons Row
# ======================

btn_frame = ttk.Frame(root)
btn_frame.pack(pady=20)

# ======================
# Add Expense Window
# ======================

def add_expense():
    add_window = tk.Toplevel(root)
    add_window.title("Add Expense")
    add_window.geometry("350x280")
    add_window.resizable(False, False)

    container = ttk.Frame(add_window, padding=20)
    container.pack(fill="both", expand=True)

    ttk.Label(
        container,
        text="Add New Expense",
        font=("Segoe UI", 13, "bold")
    ).pack(pady=(0, 15))

    # Payer
    ttk.Label(container, text="Who paid?").pack(anchor="w")

    payer_var = tk.StringVar()
    payer_entry = ttk.Entry(container, textvariable=payer_var)
    payer_entry.pack(fill="x", pady=5)

    payer_entry.focus()

    # Amount
    ttk.Label(container, text="Amount").pack(anchor="w")
    amount_entry = ttk.Entry(container)
    amount_entry.pack(fill="x", pady=5)

    # Category
    ttk.Label(container, text="Category").pack(anchor="w")
    category_combo = ttk.Combobox(
        container,
        values=["Rent", "Food", "Utilities", "Fun", "Other"],
        state="readonly"
    )
    category_combo.current(0)
    category_combo.pack(fill="x", pady=5)

    # Submit
    def submit():
        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                raise ValueError

            expense = Expense(
                payer_var.get(),
                amount,
                category_combo.get(),
                str(date.today())
            )

            budget.addExpense(expense)
            saveBudgetToFile(budget)
            update_summary()
            add_window.destroy()

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid positive number for the amount."
            )

    ttk.Button(
        container,
        text="Add Expense",
        command=submit
    ).pack(pady=15)

# ======================
# Main Buttons (ACTUALLY HERE)
# ======================

ttk.Button(
    btn_frame,
    text="➕ Add Expense",
    width=18,
    command=add_expense
).grid(row=0, column=0, padx=10)

ttk.Button(
    btn_frame,
    text="📊 View Balances",
    width=18,
    command=lambda: show_balances()
).grid(row=0, column=1, padx=10)

# ======================
# Balances Popup
# ======================

def show_balances():
    balances = calculateNewBalance(budget.totalSpent(), budget.monthlyBudget)

    lines = []
    for user, balance in balances.items():
        status = "is owed" if balance > 0 else "owes"
        lines.append(f"{user} {status} ${abs(balance):.2f}")

    messagebox.showinfo("Balances", "\n".join(lines))

# ======================
# Footer
# ======================

footer = ttk.Label(
    root,
    text="Data is saved automatically",
    font=("Segoe UI", 9),
    foreground="gray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
