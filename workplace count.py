
# Doing Math with Python.

quantity = 30
junior = 13
developer = 7
senior = 10

total = junior + developer + senior

# Now let's print the total number of employees.

print(f"The workplace quantity is {quantity}. There is {junior} junior developers."
      f" There is {developer} developers. There is {senior} senior developers."
      f" The total number of employees is {total}.")

print(f"There is a total of {total} employees in the workplace.")

# That is how you can use Python to do Math and print the results in a sentence format.

# You can also calculate years of experience in the workplace using Python.

total_experience = (junior * 1) + (developer * 3) + (senior * 5)

print(f"The total years of experience in the workplace is {total_experience}.")

# Once we have the total years of experience, we can calculate the average years of experience in the workplace.

average_experience = total_experience / total

print(f"The average years of experience in the workplace is {average_experience}.")

# As a result, we can use Python to calculate the total years of experience and the average years of experience in the workplace.

# Now, let's calculate new workers in the workplace using Python. Let's say the total count of employees in five years will be 60.

new_workers = 60 - total

print(f"The total number of new workers in the workplace in five years will be {new_workers}.")

# Now what is the total gonna be in ten years? Let's say the total count of employees in ten years will be 90.

total_in_ten_years = 90 - total

print(f"The total number of new workers in the workplace in ten years will be {total_in_ten_years}")

# That is how you can calculate workplace counts in Python by roles, experience, new workers, and future total counts.
