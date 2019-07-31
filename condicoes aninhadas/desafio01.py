house_value = float(input("How much is the house? "))
salary = float(input("What's your salary? "))
portion = int(input("How old do you want to pay? "))

payment = house_value / portion
thirty_percent = salary * 0.3

if payment > thirty_percent:
    print(f"You can't pay this amount! ${payment :.2f}")
else:
    print(f"The value of the parcels is ${payment :.2f}")

