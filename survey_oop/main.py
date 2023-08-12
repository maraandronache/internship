from Survey import Survey
from Question import InvalidInput
from Question import Question
from ValidationUtil import ValidationUtil
from AnalyzeData import AnalyzeData



# calls methods from Survey in order for the code to actually run
if __name__ == "__main__":
    survey = Survey()
    analysis = AnalyzeData()
    analysis.analyze_data()
    try:
        survey.ask_basic_info()
        survey.save_to_database()
        want_analysis = Question("Thank you for your time! Would you want to see a detailed analysis of the data"
                                 " collected in this survey? ", ValidationUtil.validate_yes_or_no).ask()
        if want_analysis == "yes":
            analysis = AnalyzeData()
            analysis.analyze_data()
    except InvalidInput as error:
            print(error)
