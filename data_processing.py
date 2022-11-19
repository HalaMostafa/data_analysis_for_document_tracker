
import os
import json
import pandas as pd

class dataProcessing:
    def __init__(self):
        self.df = pd.DataFrame
        #this dictionary to report file status
        self.cases = {
            "success":"File Uploaded Successfuly",
            "badFile":"Could not load file",
            "noLikes":"Could not find any 'also likes' documents",
            "invalidTask":"Invalid task name. Please type -h for usage info",
            "invalidDocumentId":"Could not find any results with the specified user and document id"
            }


    def getData(self,file_path: str,display):
        """Reads a json file from path, then use this to create pandas df
        - Parameters:
            - file_path: The file path of the json to read
            -display:A DisplayData object (needed to print errors to gui console)
        - Return:
            - A ReturnStatus indicating if the file was loaded successfully or not
        """
        fileCase = self.cases
        fileName = os.path.basename(file_path)# file name will be used in GUI in case of errors with it
        try:
            with open(file_path,'r') as f:
                data = json.loads("[" + 
            f.read().replace("}\n{", "},\n{") + "]")
            self.df = pd.DataFrame(data = data[0],index=[0])
            f.close()
            return fileCase["success"]
        except IOError as e:  # catch IO exceptions
            display.log(f"Unable to load file {fileName} Reason: {str(e)}")
            return fileCase["badFile"]
        except Exception as e:  # catch all other exceptions
            display.log("An error occurred while reading " + fileName + ". Reason: " + str(e))
            return fileCase["badFile"]
    
