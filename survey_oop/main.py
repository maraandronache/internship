from Survey import Survey
from Question import InvalidInput
from ReadData import ReadData


# calls methods from Survey in order for the code to actually run
if __name__ == "__main__":
    survey = Survey()
    m = ReadData()
    m.get_data()
    try:
        survey.ask_basic_info()
        survey.write()
    except InvalidInput as error:
        print(error)
