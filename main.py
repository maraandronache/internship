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
gender_tuple = ("male", "female")

while True:
    gender = input("What is your gender? ")
    # search for input in gender_tuple
    if gender.lower() in gender_tuple:
        break

education_tuple = ("middle school", "high school", "college", "bachelor degree", "master degree", "phd")

while True:
    education = input(
        "What type of education did you finish last? (middle school, high school, bachelor degree, master degree, PhD) ")
    # searching for input in education_tuple
    if education.lower() in education_tuple:
        break

# prints the report
print(f"The respondent is {age} years old, {gender.lower()}, from {city} city. The highest level of education they "
      f"have finished is {education.lower()}.")

while True:
    pets = input("Do you own pets? ")
    # checks that the user has inputted a clear yes/no answer
    if pets.lower() == 'yes' or pets.lower() == 'y' or pets.lower() == 'no' or pets.lower() == 'n':
        break

if pets.lower() == 'yes' or pets.lower() == 'y': # continues asking questions based on the previous answer
    while True:
        no_pets = input("How many pets do you own? ")
        if no_pets.isnumeric(): # checks the input for no_pets is a number
            break
    pet_dict = {} # creates a dictionary so both the name and the specie of pets can be stored
    for i in range(int(no_pets)):
        name = input("What is the name of your pet? ")
        name = name.capitalize() # capitalizes first letter of the pet name
        specie = input(f"What specie is {name}? ")
        pet_dict[name] = specie # adds name and specie to the dictionary
else:
    while True:
        adopt = input("Are you open to the idea of owning pets? ")
        # checks the answer is a clear yes or no
        if adopt.lower() == 'yes' or adopt.lower() == 'y' or adopt.lower() == 'no' or adopt.lower() == 'n':
            break
    # asks final questions based on the previous answer
    if adopt.lower() == 'yes' or adopt.lower() == 'y':
        issue = input("What is stopping you from buying or adopting some? ")
    else:
        ch_mind = input("What would change your mind? ")
