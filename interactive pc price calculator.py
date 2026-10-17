
# Interactive PC Part Calculator with input and functions.

# In this mini-project, I will be adding inputs, functions, and more refined enhancements from my previous project, pc  price calculator.py

# This program offers interactable inputs and catches errors when the user enters an invalid and illegal answer.

def get_parts_from_user():
    """Let the user enter part names and prices until they're done."""
    parts = {}
    print("Enter your PC parts (type 'done' when finished)\n")

    while True:
        name = input("Part name: ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("Part name can't be empty.\n")
            continue

        price = get_price()
        parts[name] = price
        print(f"Added {name}: ${price:.2f}\n")

    return parts

# The code above makes the user input their component and the price of the component they enter. This combines four fundamentals in Python.
