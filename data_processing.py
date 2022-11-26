
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

    def getFileName(self,file_path):
        return os.path.basename(file_path)# file name will be used in GUI in case of errors with it

    def getData(self,file_path: str,display):
        """Reads a json file from path, then use this to create pandas df
        - Parameters:
            - file_path: The file path of the json to read
            -display:A DisplayData object (needed to print errors to gui console)
        - Return:
            - A ReturnStatus indicating if the file was loaded successfully or not
        """
        fileCase = self.cases
        fileName = self.getFileName(file_path)
        try:
            with open(file_path,'r') as f:
                data = json.loads("[" + 
            f.read().replace("}\n{", "},\n{") + "]")
            self.df = pd.json_normalize(data = data) #dependent keys null values incase of not applicable
            f.close()
            return fileCase["success"]
        except IOError as e:  # catch IO exceptions
            display.log(f"Unable to load file {fileName} Reason: {str(e)}")
            return fileCase["badFile"]
        except Exception as e:  # catch all other exceptions
            display.log("An error occurred while reading " + fileName + ". Reason: " + str(e))
            return fileCase["badFile"]



# views by browser

# import httpagentparser

# df['browser_name'] = df["visitor_useragent"].apply(lambda row: httpagentparser.detect(row)['browser']['name'])
# print(df['browser_name'].unique())
# ex = """Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0;\
#      SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; AskTbORJ/5.15.9.29495; .NET4.0C)"""
# print(httpagentparser.detect(ex)['browser']['name'])
# # df['browser_name']= result.apply(lambda row: row['browser']['name'])
# # df['browser_version']= result.apply(lambda row: row['browser']['version'])
# # df['os_name']= result.apply(lambda row: row['os']['name'])
# # df['os_version']= result.apply(lambda row: row['os']['version'])
# # print(result.shape)
# # print("-------------------------------")
# # for col in ['browser_name','browser_version','os_name','os_version']:
# #     print(df[col].unique())
# #     print("-------------------------------")


#Also likes

