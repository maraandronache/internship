from Survey import Survey
from Question import InvalidInput
import mysql.connector
print(mysql.connector.__version__)

# calls methods from Survey in order for the code to actually run
if __name__ == "__main__":
    survey = Survey()
    try:
        survey.ask_basic_info()
        survey.write()
    except InvalidInput as error:
        print(error)
