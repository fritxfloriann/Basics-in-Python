# Doing Lists in Python

# Instead of the traditional method of doing variables, we will be making it into one list.

languages = ["English", "Mandarin", "German", "Spanish"]

# This is much cleaner than typing each languages in separate variables.

# And Python uses indexing for each variable.

print(languages[0])

# This should print the first variable, which is English.

print(languages[1])

# With the second print, this should say Mandarin.

# Now let's try adding items in a list, or should I say, appending.

programming_languages = ["Python", "C#", "C+"]

print(programming_languages[0])

# This should say Python, but what if we want to add another programming language? We will use append to add variables in the list,

programming_languages.append("JavaScript")

print(programming_languages)

# The new variable, "JavaScript", should be added to the list of variables.

# You also keep adding variables to the list.

programming_languages.append("Assembly")

programming_languages.append("C++")

print(programming_languages)

# You can continuously add variables into a list by appending them, but what about removing them?

