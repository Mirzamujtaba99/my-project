# Simple Expense Logger by Mujtaba

file = open("my_expenses.txt", "a")

item = input("What did you spend on? ")
amount = input("How much did you spend? ₹ ")

file.write(f"{item} - ₹{amount}\n")
file.close()

print("Saved! ✅")
