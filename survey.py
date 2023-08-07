file = open("input.csv", 'a')

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

while True:
    inp = input("Do you own pets? (yes/no) ")
    # checks that the user has inputted a clear yes/no answer
    if inp.lower() == 'yes' or inp.lower() == 'no':
        break

if inp.lower() == 'yes':  # changes the input into a boolean variable
    has_pets = True
else:
    has_pets = False

# prints report depending on the previous answer (if they do or do not own pets)
if has_pets:
    print(f"The respondent is {age} years old, {gender.lower()}, from {city} city. The highest level of education they "
          f"have finished is {education.lower()} and they own pets.")
else:
    print(f"The respondent is {age} years old, {gender.lower()}, from {city} city. The highest level of education they "
          f"have finished is {education.lower()} and they do not own pets.")

file.write(age + ',' + city + ',' + gender + ',' + education + ',')
file.write(f"{has_pets}")

if has_pets:  # continues asking questions based on the previous answer
    while True:
        no_pets = input("How many pets do you own? ")
        if no_pets.isnumeric():  # checks the input to make sure no_pets is a number
            break
    file.write(f",{no_pets}")
    pet_dict = {}  # creates a dictionary so both the name and the type of pet can be stored
    for i in range(int(no_pets)):
        name = input("What is the name of your pet? ")
        name = name.capitalize()  # capitalizes first letter of the pet name
        type = input(f"What type of pet is {name}? ")
        pet_dict[name] = type  # adds name and type to the dictionary
        file.write(',' + name + ',' + type.lower())
else:
    while True:
        open_to_adopt = input("Are you open to the idea of owning pets? ")
        # checks the answer is a clear yes or no
        if open_to_adopt.lower() == 'yes' or open_to_adopt.lower() == 'y' or open_to_adopt.lower() == 'no' or \
                open_to_adopt.lower() == 'n':
            break
    file.write(',' + open_to_adopt)
    # asks final questions based on the previous answer
    if open_to_adopt.lower() == 'yes' or open_to_adopt.lower() == 'y':
        issue = input("What is stopping you from buying or adopting some? ")
        file.write(',' + issue)
    else:
        change_mind = input("What would change your mind? ")
        file.write(',' + change_mind)


file.write('\n')