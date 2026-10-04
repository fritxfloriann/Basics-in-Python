
# if and else function

role = "Software Developer"

if role == "Software Developer":
    print ("Access granted.")
else:
    print ("Access denied.")

# The bottom shows the else function, which is used to execute a block of code if the condition in the if statement is false.

role = "Junior Software Developer"

if role == "Software Developer":
    print ("Access granted.")
else:
    print("Access denied.")

# The if and else function is a conditional statement that allows you to execute different blocks of code based on whether a condition is true or false.

# But you can also use the elif function, which is short for "else if".

role = "Junior Software Developer"

if role == "Software Developer":
    print ("Access granted.")

elif role == "Junior Software Developer":
    print("Access granted, but with limited permissions.")

else:
    print("Access denied.")

# Finally, the else function is when the condition in the if statement is false, and the elif function is false.

role = "Intern"

if role == "Software Developer":
    print("Access granted.")

elif role == "Junior Software Developer":
    print("Access granted, but with limited permissions.")

else:
    print("Access denied.")

# This will result in the output "Access denied." because the role is "Intern, which does not match any of the conditions in the if or elif statements.
