while True:
    age = input("What is your age? ")
    # using the isnumeric function to check if every character is a number in order to validate age input
    if age.isnumeric():
        break

while True:
    city = input("What city are you from? ")
    # using the isalpha function to check if every character is in the alphabet in order to validate city
    if city.isalpha():
        break

# tuple for the genders, including the other option
gender_tuple = ("male", "female", "transgender", "non-binary", "gender neutral", "gender fluid", "other")

while True:
    gender = input("What is your gender? (male/ female/ gender neutral/ gender fluid/ other) ")
    #searchs for input in gender_tuple
    if gender.lower() in gender_tuple:
        break

education_tuple = ("middle school", "high school", "college", "bachelor degree", "master degree", "phd")

while True:
    education = input(
        "What type of education did you finish last? (middle school, high school, bachelor degree, master degree, PhD) ")
    #searching for input in education_tuple
    if education.lower() in education_tuple:
        break

while True:
    pets = input("Do you own pets? ")
    # checks that the user has inputted a clear yes/no answer
    if pets == 'yes' or pets == 'y' or pets == 'Yes' or pets == 'no' or pets == 'n' or pets == 'No':
        break

# prints the report
print(f"The respondent is {age} years old, {gender.lower()}, from {city} city. The highest level of education they have finished is {education.lower()}.")

