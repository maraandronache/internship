class ValidationUtil:
    @staticmethod
    def validate_number(x):
        return x.isnumeric()

    @staticmethod
    def validate_city(x):
        return x.isalpha()

    @staticmethod
    def validate_gender(x):
        gender = ("male", "female")
        return x.lower() in gender

    @staticmethod
    def validate_education(x):
        education = ("middle school", "high school", "college", "bachelor degree", "master degree", "phd")
        return x in education

    @staticmethod
    def validate_yes_or_no(x):
        yes_no = ("yes", "no")
        return x.lower() in yes_no
