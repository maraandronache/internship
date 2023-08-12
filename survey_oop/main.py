from Survey import Survey
from Question import InvalidInput
from Question import Question
from ValidationUtil import ValidationUtil
from AnalyzeData import AnalyzeData
from Server import MyServer
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080


# calls methods from Survey in order for the code to actually run
if __name__ == "__main__":

    # webServer = HTTPServer((hostName, serverPort), MyServer)
    # print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        # try:
        #     webServer.serve_forever()
        # except KeyboardInterrupt:
        #     pass
        # webServer.server_close()
        # print("Server stopped.")
        for i in range(5000):
            print(i)
            survey = Survey()
            survey.generate_random_answers()
            survey.save_to_database()

        want_analysis = Question("Thank you for your time! Would you want to see a detailed analysis of the data"
                                 " collected in this survey? ", ValidationUtil.validate_yes_or_no).ask()
        if want_analysis == "yes":
            analysis = AnalyzeData()
            analysis.analyze_data()
    except InvalidInput as error:
            print(error)
