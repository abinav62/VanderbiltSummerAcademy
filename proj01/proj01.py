# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

user_input = raw_input("What is your name?")
user_input2 = raw_input("When is your birthday? (e.g., May 27)")
user_input3 = raw_input("What year were you born in?")
derp = int(user_input3)
years = int(user_input3) + 100
age = 2017 - derp
user_input4 = raw_input("Have you had a birthday this year? (Yes or no):")
if user_input4 == "yes":
    pass
else:
    years = years - 1
if age < 100:
    print "You will be 100 years old on " + user_input2 + " in " + str(years)
else:
    print "You were 100 years old on " + user_input2 + " in " + str(years)


if age > 17:
    print "You can watch all types of movies without parental guidance."
if age == 17:
    print "You can watch G, PG, PG-13, and R movies wthout parental guidance."
if age < 17 and age >= 13:
    print "You can watch G, PG, and PG-13 movies without parental guidance. You can also watch R movies, but with parental guidance."
if age < 13:
    print "You can watch G and PG movies without guidance, but this depends on the parents. However, you mus watch PG-13 movies with parental guidance."