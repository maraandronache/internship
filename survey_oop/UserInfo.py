from Question import Question
from QuestionsEnum import QuestionEnum


class UserInfo:
    def __init__(self):
        self.age = Question(QuestionEnum.Q1.value, validation=lambda x: x.isnumeric()).ask()
        self.city = Question(QuestionEnum.Q2.value, validation=lambda x: x.isalpha()).ask()
        self.gender = Question(QuestionEnum.Q3.value, validation=lambda x: x.lower() in QuestionEnum.GENDER.value).ask()
        self.education = Question(QuestionEnum.Q4.value, validation=lambda x: x.lower() in
                                                                              QuestionEnum.EDUCATION.value).ask()
        if Question(QuestionEnum.Q5.value, validation=lambda x: x.lower() in QuestionEnum.YESNO.value).ask() == "yes":
                self.has_pets = True
        else:
                self.has_pets = False
        self.open_to_adopt = None
        self.issue = None
        self.change_mind = None
        self.no_of_pets = 0
        self.pet_dict = {}


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


    def get_more_info(self):
        if self.has_pets:
            self.no_of_pets = Question(QuestionEnum.Q6.value, validation=lambda x: x.isnumeric()).ask()
            self.store_pet_info()
        else:
            self.open_to_adopt = Question(QuestionEnum.Q9.value,
                                          validation=lambda x: x.lower() in QuestionEnum.YESNO.value).ask()
            if self.is_open_to_adopt:
                self.issue = Question(QuestionEnum.Q10.value).ask()
            else:
                self.change_mind = Question(QuestionEnum.Q11.value).ask()


    def store_pet_info(self):
        for i in range(int(self.no_of_pets)):
            name = Question(QuestionEnum.Q7.value, validation=None).ask()
            name = name.capitalize()
            type = Question(QuestionEnum.Q8.value).ask()
            self.pet_dict[name] = type.lower()


    def write_input(self):
        with open("collected_data.csv", 'a') as file:
            file.write(f"{self.age},{self.city},{self.gender},{self.education},{self.has_pets},")
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