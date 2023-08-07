import csv

class CollectingData:
    def __init__(self, file):
        self.file = file
        self.data = self.get_data()

    def get_data(self):
        with open(self.file, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data

    def get_all_ages:


m = CollectingData("collected_data.csv")
print(m.data)