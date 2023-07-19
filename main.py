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

gender = input("What is your gender? ")
education = input("What type of education did you finish last? (middle school, high school, college, masters, PhD, etc.) ")

while True:
    pets = input("Do you own pets? ")
    # checks that the user has inputted a clear yes/no answer
    if pets == 'yes' or pets == 'y' or pets == 'Yes' or pets == 'no' or pets == 'n' or pets == 'No':
        break

# prints the report
print(f"The respondent is {age} years old, {gender}, from {city} city. The highest level of education they have finished is {education}.")

