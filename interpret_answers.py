import csv


def main():
    all_ages = []  # list in which we add all the ages
    owners_ages = []  # list in which we put all the pet owners' ages
    non_owners_ages = []  # list in which we put all the non pet owners' ages
    pet_types = []
    pet_names = []
    male_cnt = 0
    female_cnt = 0
    with open("input.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            all_ages.append(int(row[0]))
            # seeing how many people own/do not own pets
            if row[4] == 'True':
                owners_ages.append(int(row[0]))
                num = int(row[5])
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
    percentage_owners = round(percentage(owns_pets, not_owns_pets), 2)

    report.write(f"A total number of {total_resp} people have taken this survey, out of which {owns_pets} own pets and "
                 f"{not_owns_pets} do not.\n")
    report.write(f"Overall, about {percentage_owners}% own pets, and {100-percentage_owners}% do not.")


def average(list):
    sum = 0
    for x in list:
        sum += int(x)

    return sum/len(list)

def percentage(a, b):
    return a * 100 / (a + b)



main()

