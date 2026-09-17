# AP, your budget assignment

while True:
    try:
        income = float(input("What is you monthly income?:"))
        break
    except:
        print("Please enter a valid number for your income:")
  
while True:
    try:
        rent = float(input("What is your monthly rent cost?:"))
        break
    except:
        print("Please enter a valid number for your rent:")      
        
while True:
    try:
        utilities = float(input("What is your monthly utilities cost?:"))
        break
    except:
        print("Please enter a valid number for your utilities cost")

while True:
    try:
        groceries = float(input("What is you monthly groceries cost?:"))
        break
    except:
        print("Please enter a valid number for you groceries cost")
        
while True:
    try:
        transportation = float(input("What is you monthly transportation cost?:"))
        break
    except:
        print("Please enter a valid number for your transportation cost")
while True:
    try:
        savings = float(input("What is you monthly savings cost?:"))
        break
    except:
        print("Please enter a valid number for your savings cost")

print(f"Your monthly rent is ${rent:.2f} {int(rent/income*100)}%")
print(f"Your monthly utilities cost is ${utilities:.2f} {int(utilities/income*100)}%")
print(f"Your monthly groceries cost is ${groceries:.2f} {int(groceries/income*100)}%")
print(f"Your monthly transportation cost is ${transportation:.2f} {int(transportation/income*100)}%")
print(f"Your monthly savings cost is ${savings:.2f} {int(savings/income*100)}%")
