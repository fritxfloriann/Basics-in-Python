# Today, I used a simple command of greeting to learn formatting and tons of fundamentals.

name = input("What is your name? ").strip().title()

if not name:
    name = "User"

print(f"\nHello, {name}!")
print(f"Welcome to Python, {name}!")

age_input = input(f"By the way, {name}, how old are you? ")

if age_input.isdigit():
    age = int(age_input)
    future_age = age + 10
    print(f"In 10 years, you will be {future_age} years old. Time flies when you're coding!")
else:
    print("It's okay to not share your age, I respect that!")
