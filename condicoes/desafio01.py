from random import randint

print("Try guess a number on 0 to 5.")

user_num = int(input("What is your guess? "))
cpu_num = randint(0, 5)

if user_num == cpu_num:
    print(f"You're RIGHT! The number is {cpu_num}, CONGRATULATIONS!")
else:
    print(f"You MISSED! The number was {cpu_num}. ")
