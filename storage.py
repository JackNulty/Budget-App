import json

from budget import Budget, Expense

def saveBudgetToFile(t_budget, t_filename="data.json"):
    data = {
        "monthlyBudget" : t_budget.monthlyBudget,
        "expenses" : [e.to_dict() for e in t_budget.expenses]
    }
    with open(t_filename, "w") as f:
        json.dump(data, f, indent=4)

def loadBudgetFromFile(t_filename="data.json"):
    try:
        with open(t_filename, "r") as f:
            data = json.load(f)
        budget = Budget(data["monthlyBudget"])
        for e in data["expenses"]:
            budget.addExpense(Expense(**e))
        return budget
    except FileNotFoundError:
        return None