class Budget:
    def __init__ (self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        """
            To convet parameters to string and putput in a table - like format
        """
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
            #items += item['description'] + item['amount'] + '\n'
            total += item['amount']

        output = title + items + "Total: " + str(total)
        return output

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description":description})
            return True
        return False

    def balance(self):
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]
        return total_cash

    def transfer (self, amount, category):
        if(self.check_funds(amount)):
            self.withdraw(amount,"Transfer to " + category.name)
            category.deposit(amount, "Transfer from" + self.name)
            return True
        return False

    def check_funds(self, amount):
        if(self.balance() >= amount):
            return True
        return False
    
