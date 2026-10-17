
# Interactive PC Part Calculator with input and functions.

# In this mini-project, I will be adding inputs, functions, and more refined enhancements from my previous project, pc  price calculator.py

# This program offers interactive inputs and catches errors when the user enters an invalid or illegal answer.

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

# IMPORTANT !! Type done once you're done answering the questions provided.

# Below is how Python handles errors, loops, functions, and how it computes.

import math

def get_price():
    """Keep asking until the user enters a valid, non-negative price."""
    while True:
        raw = input("Price: $").strip()

        try:
            price = float(raw)

            if not math.isfinite(price):
                print("Please enter a finite number.")
                continue

            if price < 0:
                print("Price can't be negative.")
                continue

            return price

        except ValueError:
            print("Please enter a valid number.")
