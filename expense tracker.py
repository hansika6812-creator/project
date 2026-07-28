expenses = []

n = int(input("Enter number of expenses: "))

for i in range(n):
    amount = float(input("Enter expense: "))
    expenses.append(amount)

print("Total Expense =", sum(expenses))

