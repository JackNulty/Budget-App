class Expense:
    def __init__(self, t_payer, t_amount, t_category, t_date, t_description=""):
        self.payer = t_payer
        self.amount = t_amount
        self.category = t_category
        self.date = t_date
        self.description = t_description
    
    def to_dict(self):
        return self.__dict__
    
class Budget:
    def __init__(self, t_monthlyBudget):
        self.monthlyBudget = t_monthlyBudget
        self.expenses = []

    def addExpense(self, t_expense):
        self.expenses.append(t_expense)

    def totalSpent(self):
        return sum(expense.amount for expense in self.expenses)
    
    def remainingBudget(self):
        return self.monthlyBudget - self.totalSpent()