from budget import Budget, Expense
from calculations import calculateNewBalance
from storage import saveBudgetToFile, loadBudgetFromFile    
from ui import mainMenu
from datetime import date

budget = loadBudgetFromFile() or Budget(1500)

while True:
    choice = mainMenu()

    if choice == "1":
        payer = input("Enter payer name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        expense = Expense(payer, amount, category, str(date.today()), description)
        budget.addExpense(expense)
        print("Expense added successfully.")

    elif choice == "2":
        print("Total Expenses: ", budget.totalSpent())
        print("Remaining Budget: ", budget.remainingBudget())

    elif choice == "3":
        newBalance = calculateNewBalance(budget.totalSpent(), budget.monthlyBudget)
        print("Current Balance: ", newBalance)

    elif choice == "4":
        saveBudgetToFile(budget)
        print("Budget saved. Exiting...")
        break