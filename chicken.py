# Now, let's do multiplication involving chickens and eggs.

chicken = 4
eggs = 2

# Assuming each chicken lays two eggs each.

total = (chicken * eggs)
fullygrown = (total + chicken)

print(f"There are {chicken} at the hen. Each will lay {eggs}. How many chicks would be born?")
print(f"If all eggs beared a chick, that would equal to {total} chicks")
print(f"And after the {total} chicks grew up, there will be {fullygrown} chickens.")

# We now have the total chickens counted. This is how Python calculates math.

# Let's take it a step further and now use turkey and servings for each person.

# And yes, this is intentional.

# Assuming each person takes one piece from the turkey.

turkeypcs = 8
people = 4

serving = (turkeypcs - people)

print(f"At a party, {people} people came and there were {turkeypcs} turkey pieces.")
print(f"Each person took one big piece. After serving, there were {serving} turkey pieces left.")
print(f"The rest ate the remaining servings, which had {serving} remaining.")

# This should serve the purpose of how Python does subtraction, while also serving guests the correct serving.
