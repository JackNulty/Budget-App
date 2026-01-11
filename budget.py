class Expense:
    def __init__(self, payer, amount, category, date, description=""):
        self.payer = payer
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
    
    def to_dict(self):
        return {
            "payer": self.payer,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }
    
class Budget:
    def __init__(self, monthlyBudget):
        self.monthlyBudget = monthlyBudget
        self.expenses = []

    def addExpense(self, expense):
        self.expenses.append(expense)
        
    def totalSpent(self):
        return sum(expense.amount for expense in self.expenses)
    
    def remainingBudget(self):
        return self.monthlyBudget - self.totalSpent()