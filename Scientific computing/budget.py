"""In function, fix % finder"""


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.__balance = 0.00

    def __repr__(self):
        header = self.name.center(30, "*") + "\n"
        sheet = ""
        for item in self.ledger:
            description = item["description"][:23]
            description_length = len(description)
            amount = float(str(round(item["amount"], 2))[:7])
            amount = str("%.2f" % amount)
            line = description + amount.rjust(30 - description_length)
            sheet = sheet + line + "\n"

        total = "Total: " + str(self.__balance)
        return header + sheet + total

    def deposit(self, value, name=""):
        deposit = {"amount": value, "description": name}
        self.ledger.append(deposit)
        self.__balance += float(value)

    def withdraw(self, value, name=""):
        if self.check_funds(value):
            value = 0 - value
            withdraw = {"amount": value, "description": name}
            self.ledger.append(withdraw)
            self.__balance += float(value)
            return True
        else:
            return False

    def get_balance(self):
        return self.__balance

    def transfer(self, value, target_category):
        if self.withdraw(value, "Transfer to " + str(target_category.name)):
            target_category.deposit(value, "Transfer from " + str(self.name))
            return True
        else:
            return False

    def check_funds(self, value):
        if self.__balance - value >= 0.0:
            return True
        else:
            return False


def create_spend_chart(categories):
    total_spend = 0
    category_dict = {}
    graph = ""
    for category in categories:
        category_spend = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_spend += int(item["amount"])
            category_dict[category.name] = 0 - category_spend
            total_spend += -category_spend

    for name in category_dict:

        category_dict[name] = int((category_dict[name] / total_spend) * 10)

        # Here python is only rounding down. Fix this!
        # print(name, category_dict[name])

    graph += "Percentage spent by category\n"
    for value in reversed(range(0, 101, 10)):
        graph += str(value).rjust(3) + "| "
        for name in category_dict:
            if category_dict[name] * 10 >= value:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    graph += "    " + "-" * ((3 * len(categories)) + 1)
    # Figuring out how to get to the right spacing. . .
    steps = 0
    for key in category_dict:
        if len(key) > steps:
            steps = len(key)

    for step in range(steps):
        graph += "\n" + "     "
        for key in category_dict:
            try:
                graph += key[step] + "  "
            except:
                graph += " " + "  "

    return graph


Fuel = Category("Fuel")
Fuel.deposit(10000, "I'm rich Bitch!")
Fuel.withdraw(200, "Vroom Vroom")
print(Fuel)

Food = Category("Food")
Food.deposit(10000)
Food.withdraw(300)

Rent = Category("Rent")
Rent.deposit(10000)
Rent.withdraw(500)

Entertainment = Category("Entertainment")
Entertainment.deposit(1000)
Entertainment.withdraw(200)


print(create_spend_chart(([Fuel, Food, Rent, Entertainment])))
