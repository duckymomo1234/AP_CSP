# AP, Functions notes
def stupid_proof(money):
    while True:
        try:
            amount = float(input(f"What is your monthly {money}:"))
            return amount
        except:
            print("That isnt a number! :(")

# write all your variables
income = stupid_proof("income")
rent = stupid_proof("rent")
utilities = stupid_proof("utilities")
groceries = stupid_proof("groceries")
transportation = stupid_proof("transportation")
savings = income * .1

# write any function your are using
def calc_percent(income, bill):
    return round(bill/income *100)

# Outputs for user
print(f"Your rent is ${rent:.2f} that is {calc_percent(income,rent)}% of your income.")
print(f"Your rent is ${utilities:.2f} that is {calc_percent(income,utilities)}% of your income.")
print(f"Your rent is ${groceries:.2f} that is {calc_percent(income,groceries)}% of your income.")
print(f"Your rent is ${transportation:.2f} that is {calc_percent(income,transportation)}% of your income.")
print(f"You should save ${savings:.2f} that is {calc_percent(income,savings)}% of your income.")
print(f"You have ${income-rent-utilities-groceries-transportation-savings:.2f} left to spend!")



