
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

# Now let's analyse what the impact would be if the total 30 workers worked 48 hours a week.

hours_per_worker_per_week = 48

standard_hours_per_worker_per_week = 40

weeks_per_year = 52

weekly_team_hours = total * hours_per_worker_per_week

standard_weekly_team_hours = total * standard_hours_per_worker_per_week

# Now, let's include additional time frames for each team and employees.

additional_weekly_hours = weekly_team_hours - standard_weekly_team_hours

additional_hours_per_worker = hours_per_worker_per_week - standard_hours_per_worker_per_week
annual_team_hours = weekly_team_hours * weeks_per_year

annual_additional_hours = additional_weekly_hours * weeks_per_year

full_time_equivalent_workers = weekly_team_hours / standard_hours_per_worker_per_week

increase_percent = (additional_weekly_hours / standard_weekly_team_hours) * 100

# And let's print the calculations.

print(f"If all {total} workers work {hours_per_worker_per_week} hours per week, "
      
      f"the team works {weekly_team_hours} hours per week.")

print(f"Compared with a {standard_hours_per_worker_per_week}-hour week, that is "
      
      f"{additional_hours_per_worker} extra hours per worker and "

      f"{additional_weekly_hours} extra team hours per week "

      f"({increase_percent:.0f}% more).")

print(f"Assuming this schedule continues for {weeks_per_year} weeks, the team works "
      
      f"{annual_team_hours} hours per year, including "

      f"{annual_additional_hours} hours above the 40-hour-per-worker benchmark.")

print(f"At {standard_hours_per_worker_per_week} hours per week, "
      
      f"{weekly_team_hours} hours is equivalent to "

      f"{full_time_equivalent_workers:.0f} full-time workers.")

# That is how you can calculate the work hours for the total employee count.
