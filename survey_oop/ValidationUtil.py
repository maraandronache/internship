class ValidationUtil:
    def valid_age(x):
        return x.isnumeric()
    def valid_city(x):
        return x.isalpha()

    def valid_gender(x):
        gender = ("male", "female")
        return x.lower() in gender

    def valid_education(x):
        education = ("middle school", "high school", "college", "bachelor degree", "master degree", "phd")
        return x in education

    def valid_yes_no(x):
        yes_no = ("yes", "no")
        return x.lower() in yes_no

