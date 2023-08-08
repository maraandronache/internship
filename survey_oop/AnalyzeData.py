import matplotlib.pyplot as plt
from collections import Counter


class AnalyzeData():
    def __init__(self, age_list, gender):
        self.age_list = [int(age[0]) for age in age_list]
        self.gender =[x[0] for x in gender]
    def analyze_age(self):
        plt.hist(self.age_list, edgecolor='black', width=0.3)
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.title('Age Distribution')
        plt.show()
        print(self.age_list)

    def analyze_gender(self):
        counter = Counter(self.gender)
        unique_values = list(counter.keys())
        frequencies = list(counter.values())
        plt.pie(frequencies, labels=unique_values)
        plt.axis('equal')
        plt.title('Gender Distribution')
        plt.show()



