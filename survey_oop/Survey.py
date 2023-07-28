from QuestionsEnum import QuestionEnum


class Survey:
    def __init__(self):
        self.pet_dict = {}
        self.dict = {}


    def start(self):
        self.age = QuestionEnum.ASK_AGE.value.ask()
        self.city = QuestionEnum.ASK_CITY.value.ask()
        self.gender = QuestionEnum.ASK_GENDER.value.ask()
        self.education = QuestionEnum.ASK_EDUCATION.value.ask()
        if QuestionEnum.ASK_HAS_PETS.value.ask().lower() == "yes":
            self.has_pets = True
        else:
            self.has_pets = False
        if self.has_pets:
            self.no_of_pets = QuestionEnum.ASK_NO_OF_PETS.value.ask()
            self.store_pet_info()
        else:
            self.open_to_adopt = QuestionEnum.ASK_OPEN_TO_ADOPT.value.ask()
            if self.open_to_adopt:
                self.issue = QuestionEnum.ASK_ISSUE.value.ask()
            else:
                self.change_mind = QuestionEnum.ASK_CHANGE_MIND.value.ask()

    def store_pet_info(self):
        for i in range(int(self.no_of_pets)):
            name = QuestionEnum.ASK_NAME_OF_PETS.value.ask()
            name = name.capitalize()
            type = QuestionEnum.ASK_TYPE_OF_PETS.value.ask()
            self.pet_dict[name] = type.lower()

    def add_answer(self, question, answer):
        self.dict[question] = answer

    def add_answers(self):
        self.add_answer(QuestionEnum.ASK_AGE, self.age)
        self.add_answer(QuestionEnum.ASK_CITY, self.city)
        self.add_answer(QuestionEnum.ASK_GENDER, self.gender)
        self.add_answer(QuestionEnum.ASK_EDUCATION, self.education)
        self.add_answer(QuestionEnum.ASK_HAS_PETS, self.has_pets)
        return self.dict

    def write(self):
        with open("collected_data.csv", 'a') as file:
            for x in self.dict.keys():
                file.write(f"{self.dict[x]},")
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