class Question:
    def __init__(self, prompt, validation=None):
        self.prompt = prompt
        self.validation = validation

    def ask(self):
        while True:
            answer = input(self.prompt)
            if self.validation and self.validation(answer):
                return answer


class UserInfo:
    def __init__(self):
        self.age = self.get_age()
        self.city = self.get_city()
        self.gender = self.get_gender()
        self.education = self.get_education()
        self.has_pets = self.has_pets()

    def get_age(self):
        age = Question("What is your age? ", validation=lambda x: x.isnumeric())
        return int(age.ask())

    def get_city(self):
        city = Question("What city are you from? ", validation=lambda x: x.isalpha())
        return city.ask()

    def get_gender(self):
        gender_tuple = ("male", "female")
        gender = Question("What is your gender? ", validation=lambda x: x.lower() in gender_tuple)
        return gender.ask()

    def get_education(self):
        education_tuple = ("middle school", "high school", "college", "bachelor degree", "master degree", "phd")
        education = Question("What type of education did you finish last? (middle school, high school, bachelor degree,"
                             " master degree, PhD) ", validation=lambda x: x.lower() in education_tuple)
        return education.ask()

    def has_pets(self):
        has_pets = Question("Do you have pets? ", validation=lambda x: x.lower() == "yes" or x.lower() == "no")
        answer = has_pets.ask()
        if answer == 'no':
            return False

        return True

    def summary_report(self):
        if self.has_pets:
            print(
                f"The respondent is {self.age} years old, {self.gender.lower()}, from {self.city.capitalize()} city. "
                f"The highest level of education they have finished is {self.education.lower()} and they own pets.")
        else:
            print(
                f"The respondent is {self.age} years old, {self.gender.lower()}, from {self.city.capitalize()} city. "
                f"The highest level of education they have finished is {self.education.lower()} and they do not own "
                f"pets.")

    def write_input(self):
        with open("collected_data.csv", 'a') as file:
            file.write(f"{self.age},{self.city},{self.gender},{self.education},{self.has_pets},")


class PetInfo:
    def __init__(self, has_pets):
        self.has_pets = has_pets
        self.open_to_adopt = None
        self.issue = None
        self.change_mind = None
        self.no_of_pets = 0
        self.pet_dict = {}

    def get_more_info(self):
        if self.has_pets:
            self.no_of_pets = self.get_no_of_pets()
            self.store_pet_info()
        else:
            self.open_to_adopt = self.is_open_to_adopt()
            if self.is_open_to_adopt:
                self.issue = input("What is stopping you from buying or adopting some? ")
            else:
                self.change_mind = input("What would change your mind? ")

    def get_no_of_pets(self):
        no_of_pets = Question("How many pets do you own? ", validation=lambda x: x.isnumeric())
        return no_of_pets.ask()

    def store_pet_info(self):
        for i in range(int(self.no_of_pets)):
            name = input("What is the name of your pet? ")
            name = name.capitalize()
            type = input(f"What type of pet is {name}? ")
            self.pet_dict[name] = type

    def is_open_to_adopt(self):
        open_to_adopt = Question("Are you open to the idea of owning pets? ", validation=lambda x: x == "yes" or
                                                                                                   x == "no")
        return open_to_adopt.ask()

    def write_input(self):
        with open("collected_data.csv", 'a') as file:
            if self.has_pets:
                file.write(f"{self.no_of_pets}")
                for x in self.pet_dict.keys():
                    file.write(f",{x},{self.pet_dict[x]}")
            else:
                file.write(f"{self.open_to_adopt}")
                if self.open_to_adopt:
                    file.write(f",{self.issue}")
                else:
                    file.write(f",{self.change_mind}")

            file.write("\n")


if __name__ == "__main__":
    user_input = UserInfo()
    user_input.summary_report()
    user_input.write_input()
    pet_input = PetInfo(user_input.has_pets)
    pet_input.get_more_info()
    pet_input.write_input()
