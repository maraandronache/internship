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
                f"The respondent is {self.age} years old, {self.gender.lower()}, from {self.city.capitalize()} city. The highest level of education they "
                f"have finished is {self.education.lower()} and they own pets.")
        else:
            print(
                f"The respondent is {self.age} years old, {self.gender.lower()}, from {self.city.capitalize()} city. The highest level of education they "
                f"have finished is {self.education.lower()} and they do not own pets.")

    def write_input(self):
        with open("collected_data.csv", 'a') as file:
            file.write(f"{self.age},{self.city},{self.gender},{self.education},{self.has_pets},")
