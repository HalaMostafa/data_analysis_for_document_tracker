import os
import json
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox


class dataProcessing:
    def __init__(self):
        self.df = pd.DataFrame  # initalize df
        # this dictionary to report file status
        self.cases = {
            "success": "File Uploaded Successfuly",
            "badFile": "Could not load file",
            "noLikes": "Could not find any 'also likes' documents",
            "invalidTask": "Invalid task name. Please type -h for usage info",
            "invalidDocumentId": "Could not find any results with the specified user and document id",
        }

    def getFileName(self, file_path):
        return os.path.basename(
            file_path
        )  # file name will be used in GUI in case of errors with it

    def getData(self, messagebox=messagebox):
        """Reads a json file from path, then use this to create pandas df
        - Parameters:
            - file_path: The file path of the json to read
            -display:A DisplayData object (needed to print errors to gui console)
        - Return:
            - A ReturnStatus indicating if the file was loaded successfully or not
        """
        fileCase = self.cases
        fileInput = filedialog.askopenfile(
            mode="r", filetypes=[("JSON Files", "*.json")]
        )
        if fileInput:
            try:
                with open(fileInput.name, "r") as f:
                    data = json.loads("[" + f.read().replace("}\n{", "},{") + "]")
                self.df = pd.json_normalize(
                    data=data
                )  # dependent keys null values incase of not applicable
                self.df = self.df.loc[self.df["env_type"] == "reader"]
                f.close()
                return fileCase["success"]
            except IOError as e:  # catch IO exceptions
                messagebox.showinfo(f"{str(e)}")
                return fileCase["badFile"]
            except Exception as e:  # catch all other exceptions
                messagebox.showinfo(str(e))
                return fileCase["badFile"]

    def get_sorted(self):
        doc_sort = self.df[self.df["env_type"] == "reader"]["env_doc_id"].value_counts()
        return doc_sort
