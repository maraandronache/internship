import csv


def main():
    all_ages = []  # list in which we add all the ages
    owners_ages = []  # list in which we put all the pet owners' ages
    non_owners_ages = []  # list in which we put all the non pet owners' ages
    pet_types = []
    pet_names = []
    male_cnt = 0
    female_cnt = 0
    male_owners = 0
    female_owners = 0
    with open("input.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            all_ages.append(int(row[0]))
            # seeing how many people own/do not own pets
            if row[4] == 'True':
                owners_ages.append(int(row[0]))
                num = int(row[5])
                if row[2] == 'male':
                    male_owners += 1
                else:
                    female_owners += 1
                for i in range(num):
                    pet_names.append(row[num + i + 1]) # adding all names of pets in pet_names
                    pet_types.append(row[num + i + 2])
            else:
                non_owners_ages.append(int(row[0]))
            # the overall number of male and females
            if row[2] == 'male':
                male_cnt += 1
            else:
                female_cnt += 1

    report = open("report.txt", 'a')

    total_resp = len(all_ages)
    owns_pets = len(owners_ages)
    not_owns_pets = len(non_owners_ages)
    percentage_owners = percentage(owns_pets, not_owns_pets)
    percentage_gender = percentage(male_cnt, female_cnt)
    percentage_gender_owners = percentage(male_owners, female_owners)

    report.write(f"A total number of {total_resp} people have taken this survey, out of which {owns_pets} own pets and "
                 f"{not_owns_pets} do not.\nThe average age of all the respondents is {average(all_ages)}. ")
    report.write(f"{male_cnt} males ({percentage_gender}%) and {female_cnt} females {100-percentage_gender}%) have "
                 f"answered this survey\n")
    report.write(f"Overall, about {percentage_owners}% own pets, and {100-percentage_owners}% do not.\nThe average age "
                 f"of those who own pets is {average(owners_ages)}, while the average age of those who do not is "
                 f"{average(non_owners_ages)}\n")

    if male_owners > female_owners:
        report.write(f"There are more male pet owners ({percentage_gender_owners}%) than female ones "
                     f"({100-percentage_gender_owners}%).\n")
    elif male_owners < female_owners:
        report.write(f"There are more female owners ({100-percentage_gender_owners}%) than female ones "
                     f"({percentage_gender_owners}%).\n")
    else:
        report.write("There are just as many male and female pet owners.\n")




def average(list):
    sum = 0
    for x in list:
        sum += int(x)

    return round(sum/len(list), 2)

def percentage(a, b):
    return round(a * 100 / (a + b), 2)

main()