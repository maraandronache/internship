from Question import Question
from QuestionsEnum import QuestionEnum
class UserInfo:
    def __init__(self):
        self.age = Question(QuestionEnum.Q1.value, validation=lambda x: x.isnumeric()).ask()
        self.city = Question(QuestionEnum.Q2.value, validation=lambda x: x.isalpha()).ask()
        self.gender = Question(QuestionEnum.Q3.value, validation=lambda x: x.lower() in QuestionEnum.GENDER.value).ask()
        self.education = Question(QuestionEnum.Q4.value, validation=lambda x: x.lower() in
                                                                              QuestionEnum.EDUCATION.value).ask()
        if Question(QuestionEnum.Q5.value, validation=lambda x: x.lower() == "yes" or x == "no").ask() == "yes":
            self.has_pets = True
        else:
            self.has_pets = False

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
