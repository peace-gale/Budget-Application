import Budget

food=Budget.Budget("Food")
food.deposit(1000, "Inital deposit")
food.withdraw(120, "Meat and fish")
print(food.balance())

clothing=Budget.Budget("Clothing")
food.transfer(350, clothing)
clothing.withdraw(50, "Hats")
clothing.withdraw(170, "Shoes")

rent= Budget.Budget("Rent")
rent.deposit(4500, "Intial deposit")
rent.deposit(200, "Electricity bill")

print(rent)
print("\n")
print(food)
print("\n")
print(clothing)

