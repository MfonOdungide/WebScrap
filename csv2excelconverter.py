import os
import pandas as pd
from os import system
from openpyxl import load_workbook

class File:
    
    # create the attributes of the class common to all files
    create = True
    edit = False
    exist = False
    fname = "filename"
    ext = "txt"
    exec_csv = False
    exec_xlsx = True
    full_path = os.path.realpath(__file__)

    def __init__(self,name,ext, **args): #this method will give and parse a name to the file, executed by default
        print("called by {}".format(self)) #verify who called it
        self.name = name
        self.ext = ext
        self.new_ext = "xlsx"
        self.filename = (self.name + "." + self.ext)
        self.newfilename = (self.name + "." + self.new_ext)

    def file_name(self): #this method will give and parse a name to the file
        filename = self.name + "." + self.ext
        print(filename)
        #check if the file exists and set the exist property accordingly
        pass  

    def file_path(self):
        filename = self.filename
        filepath = os.path.dirname(self.full_path) + '\\'+filename
        print(filepath)

    def file_exec(self):
        # filename = 'competitions.csv' #for test
        if File.exec_csv is True:
            try:
                filename = self.filename
                exec_path = 'C:\Windows\System32\cmd.exe /c '+ os.path.dirname(self.full_path) +'\\'+filename
                print("File execution initiated at ", exec_path)
                os.system(exec_path)
                print("File execution Successful!")
            except:
                    print ("Error executing file in path ", exec_path)

        elif File.exec_xlsx is True:
            try:

                filename = self.newfilename
                exec_path = 'C:\Windows\System32\cmd.exe /c '+ os.path.dirname(self.full_path) +'\\'+filename
                print("File execution initiated at ", exec_path)
                os.system(exec_path)
                print("File execution Successful!")
            except:
                    print("Error executing file in path ", exec_path)
        else:
            try:
                filename = input("Enter the new filename with the extension")
                exec_path = 'C:\Windows\System32\cmd.exe /c '+ os.path.dirname(self.full_path) +'\\'+filename
                print("File execution initiated at ", exec_path)
                os.system(exec_path)
                print("File Execution Successful!")
                
            except:
                    print("Error executing file in path ", exec_path)

            File.exec_xlsx = True #reset default file opening attribute

    def file_open(self):
        if File.create is False:
            print(self.name + "." + self.ext + " already exist")
            print("opening file "+ self.name + "." + self.ext + " now!")
            
        else:
            File.create = True
            print(self.name + "." + self.ext + " will be created!")
            self.file_create()
        pass

    def file_create(self,*args):
 
        if File.create is True:
            try:
                f = open(self.filename, "w")
                headers = args[0]
                f.write(str(headers) + "\n")
                f.close
                
                print(self.name + "." + self.ext + " Successfully created!")
            # except expression as identifier:
            except:
                print("Error creating "+ self.filename)
            
        else:
            File.create = False
            File.file_open()
            print(self.name + "." + self.ext + " is opened!")
 
    def file_close(self):
        f = open(self.filename, 'r') #open to read-only
        f.close #then close
        pass
           
    def file_write(self,*args):
        lines = args
        f = open(self.filename, 'a') #open to write
        # for i in lines:
        f.write("\n" + str(lines))
        print(str(lines) + " Line written successfully!")
        f.close
        
        pass
        
    def file_save(self):
        f = open(self.filename, 'a') #open to write to end of document in new line
        f.close
        pass
    
    def file_convert(self):
        filename = self.filename
        print("Filename gotten successfully as ", filename)
        newfilename = self.newfilename

        print("New Filename gotten successfully as ",newfilename)
        try:
            print(newfilename, "Initiating File Conversion...")
            read_file = pd.read_csv (filename,encoding ='UTF-8')
            read_file.to_excel (newfilename, sheet_name=self.name, index = False, header=True)
            print(newfilename, "File conversion completed Successfully!")
        except UnicodeDecodeError:
            read_file = pd.read_csv (filename, encoding ='ANSI')
            read_file.to_excel (newfilename, sheet_name=self.name, index = False, header=True)
            print("Conversion Error! File encoding mismatch with " + newfilename)
            print("File conversion completed successfully with ANSI encoding")

        except:
            read_file = pd.read_csv (filename, encoding ='ascii')
            read_file.to_excel (newfilename, sheet_name=self.name, index = False, header=True)
            print("Unknown Error was encountered converting file..." + newfilename)

        finally: #execute even if both try and except executes
            pass

def add_frame_to_workbook(file, new_sheet, dataframe):
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


### Testing Parameters ###
# myfile = File("FootyGuru_17Jan2021","csv") #turn on



# myfile.file_name()
# myfile.create


# File.create = True #turn on



# myfile.file_open()
# myfile.file_create('Winston,Churchill,Time,Season')
# myfile.file_write('create,mighty')
# myfile.file_write('Money,Absolute')
    # : use the syntax below
    # :   dt_m = method_2()
    # :   print(dt_m)
    # :   data = pd.DataFrame(dt_m)
    # :   add_frame_to_workbook(workbook,'Time4', data)
# myfile.file_path()


# myfile.file_convert() #Turn on


# File.exec_xlsx = False


# myfile.file_exec() #turn on
