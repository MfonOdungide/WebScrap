import pandas as pd
from openpyxl import load_workbook
import os
from os import system
import numpy as np


class DataSet:

    # create = True
    # edit = False
    # exist = False
    fname = "filename"
    ext = "xlsx"
    # exec_csv = False
    # exec_xlsx = True
    full_path = os.path.realpath(__file__)

    def __init__(self, workbook, worksheet, **args): #this method will give and parse a name to the file, executed by default
        print("called by {}".format(self)) #verify who called it
        # self.workbook = str(workbook+"."+self.ext)
        self.workbook = workbook
        # self.ext = ext
        # self.new_ext = "xlsx"
        self.worksheet = worksheet
        # self.filename = (self.workbook + "." + self.ext)
        # self.newfilename = (self.name + "." + self.new_ext)
        self.rawdataset = pd.read_excel(workbook, sheet_name=worksheet)
        self.df = pd.DataFrame(self.rawdataset)

        # return excel_df

    def create_dataset(self, workbook, worksheet):
        workbook = workbook
        worksheet = worksheet
        # workbook = 'FootyGuru_05DEC2020_1.xlsx'
        # workbook2 = 'FootyGuru_05DEC2020_2.xlsx'
        # sheet = 'FootyGuru'
        rawdataset = pd.read_excel(workbook, sheet_name=worksheet)
        df = pd.DataFrame(rawdataset)
        "Dataset Created Successfully!"
        return df

    def add_frame_to_workbook(self, file, new_sheet, dataframe):
        """
        Save a dataframe to a workbook tab with the filename and tabname
        coded to timestamp

        :param filename: filename to create, can use strptime formatting
        :param tabname: tabname to create, can use strptime formatting
        :param dataframe: dataframe to save to workbook
        :param timestamp: timestamp associated with dataframe
        :return: None
        : use the syntax below
        :   dt_m = method_2()
        :   print(dt_m)
        :   data = pd.DataFrame(dt_m)
        :   add_frame_to_workbook(workbook,'Time4', data)
        """

        # create a writer for this month and year
        writer = pd.ExcelWriter(file, engine='openpyxl')
        
        try:
            # try to open an existing workbook
            writer.book = load_workbook(file)
            print("Loading ", file, " workbook")
            
            # copy existing sheets
            writer.sheets = dict(
                (ws.title, ws) for ws in writer.book.worksheets)
            print("Loaded and copied all worksheets in ", file)
        except IOError:
            # file does not exist yet, we will create it
            pass

        # write out the new sheet
        dataframe.to_excel(writer, sheet_name=new_sheet, index = False)
        
        # save the workbook
        writer.save()
        print("Dataframe saved to", new_sheet, "sheet of", file, "workbook")

    def filter(self, dataframe, *args):
        data = pd.DataFrame(dataframe)
        filtered_data = data #used to maintain the original dataset/dataframe
        
        print("Sorting by", len(args),"conditions") 
        for x in args:
            # print("Condition",x)
            arguments = x.split()
            column = arguments[0]
            operation = arguments[1]
            condition = arguments[2]
            if operation == "eq":
                filter_param = (filtered_data[column] == str(condition))
                filtered_data = filtered_data.loc[filter_param]
                print("Sorting by",x)
                # print(filtered_data)
            
            elif operation =="gr":
                filter_param = (filtered_data[column] > (condition))
                filtered_data = filtered_data.loc[filter_param]
                print("Sorting by",x)
                # print(filtered_data)
            elif operation =="ls":
                filter_param = (filtered_data[column] < float(condition))
                filtered_data = filtered_data.loc[filter_param]
                print("Sorting by",x)
                # print(filtered_data)
            elif operation =="leq":
                filter_param = (filtered_data[column] <= float(condition))
                filtered_data = filtered_data.loc[filter_param]
                print("Sorting by",x)
                # print(filtered_data)
            elif operation =="geq":
                filter_param = (filtered_data[column] >= float(condition))
                filtered_data = filtered_data.loc[filter_param]
                print("Sorting by",x)
                # print(filtered_data)
            elif operation == "has":
                filter_param = (filtered_data[column].isin([condition]))
                filtered_data = filtered_data.loc[filter_param]
                print("Sorting by",x)
                # print(filtered_data)
            else:

                print("Invalid Operation")
        print("Sorting completed successfully!")
        return(filtered_data)

# Footy_filename = "FootyGuru_"+

# newfile = DataSet('FootyGuru_05DEC2020_1.xlsx','FootyGuru')
# newfileX = newfile.df
# # print (newfile.df)

# dm2 = newfile.filter(newfileX, "Time gr 10:00:00")
# newfile.add_frame_to_workbook('FootyGuru_05DEC2020_1.xlsx',"1030pmSorted",dm2)

