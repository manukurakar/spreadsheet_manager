#author : manu kurakar
# Details : Python code to manipulate csv files

import csv

class ProcessCSV:
    filename = ""
    filepath = ""
    filedetail = ""

    def __init__(self,file_name,file_path):
        # Initialize the class with file name and file path
        self.filename = file_name
        self.filepath = file_path
        self.filedetail = self.filepath + self.filename

    def combine_filename_path(self):
        # Combine file path and file name
        self.filedetail = self.filepath+self.filename

    def read_file(self):
        with open(self.filedetail,mode='rb') as csvfile:
            for row in csv.reader(csvfile.read().splitlines()):
                print row[0]+"--"+row[1]+"--"+row[2]