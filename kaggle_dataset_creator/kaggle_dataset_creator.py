
import os
import re
import pandas as pd
from messages import warning, success, error, data


class KaggleDataSetCreator(object):
    def __init__(self, 
                  path = "KaggleDataSet",
                  extension = 'csv'
                ):
        """
        A constructor
        =============
            - which initializes number of parameters to start the creation of Kaggle 
              dataset

        Parameters
        ==========
            - path: Absolute/relative path of the output file (csv, json)
            - extension: Extension to use for the output file (default: csv)
        """

        filedir, filename, extension = self.__validate_and_get(path, extension)

        self.filedir = filedir
        self.filename = filename
        self.extension = extension

        self.container = {} # Conatiner of enetered data (an input to pandas.DataFrame)
        self.total_columns = 0
        self.columns = []
        self.collens = []

        # Private variable to maintain the calling sequences
        self.__states = {}

    def __validate_and_get(self, path, extension):
        """
        Description
        ===========
            - Validates path and returuns a tuple => (filedir, filename, extension)

        Opeartions
        ==========

            >>> os.path.splitext("C:\\TC\\a.txt")
            ('C:\\TC\\a', '.txt')
            >>>
            >>> os.path.exists(".")
            True
            >>>
            >>>
            >>> re.match("^\w+(\w+[-_])*\w+$", "dffdfd-ddgg-$")
            >>> re.match("^\w+(\w+[-_])*\w+$", "dffdfd-ddgg-dffd")
            <_sre.SRE_Match object at 0x00000000029FCD50>
            >>>
            >>> re.match("^\w+(\w+[-_])*\w+$", "dffdfd-ddgg_dffd")
            <_sre.SRE_Match object at 0x00000000029FCDC8>
            >>>
            >>> re.match("^\w+(\w+[-_])*\w+$", "dffdfd_ddgg_dffd")
            <_sre.SRE_Match object at 0x00000000029FCD50>
            >>>
            >>> re.match("^\w+(\w+[-_])*\w+$", "dffdfd_ddgg+dffd")
            >>>
        """

        if path and type(path) is str:
            filedir, file_w_ext = os.path.split(path)
            filename, ext = os.path.splitext(file_w_ext)

            if ext:
                ext = ext.lstrip('.')

                if ext in ['json', 'csv']:
                    extension = ext
                else:
                    extension = 'csv'
            elif not extension in ['json', 'csv'] :
                extension = "csv"

            if not filedir:
                filedir = "."

            if not os.path.exists(filedir):
                filedir = "."

            if not re.match(r"^\w+(\w+[-_])*\w+$", filename):
                warning('Valid file names are: my-data-set, mydataset, my-data_set, mydataset.csv etc.')
                filename = "KaggleDataSet"
        else:
            filename = 'KaggleDataSet'
            filedir = "."

            if not extension in ["json", 'csv']:
                extension = 'csv'

        # Repeatedly check for an existence of specified filename, 
        # if it already exists (do not override)
        # and choose another file name by appending numbers like 1, 2, 3 and so...on
        i = 1
        while os.path.exists(os.path.join(filedir, filename + '.' + extension)):
            filename = filename + "-" + str(i);
            i = i + 1;

        return filedir, filename, extension

    def get_value_for(self, rowno, colname, max_col_len):
        """ 
        Description
        ===========
            - Returns the value entered on console
        """

        s = "[DATA ENTRY] <row " + str(rowno) + "> "
        l = len(s) + max_col_len + 4
        f = ("%-" + str(l) + "s : ") % (s + " " + colname)
        value = input(f).strip()

        return value

    def set_container(self):
        """
        Description
        ===========
            - Asks user to enter data for each rows, column by column 
            - Finally sets the container attribute of the class
        """

        done = False

        if self.__states.get('start'):
            if self.__states.get('set_column_names'):
                done = True
            else:
                warning("You are directly trying to invoke, set_container() method"
                    ", please call start() => set_column_names() methods first")
        else:
            warning("You are directly trying to invoke, set_container() method"
                    ", please call start() method first")

        if done:
            satisfied = False
            rowno = 1
            hashes =  "======================================="
            msg = "\n" + hashes + "\nDo you want to add 1 more row (y/n): "
            max_col_len =  max(self.collens)

            while not satisfied:
                for colname in self.columns:
                    value = self.get_value_for(rowno, colname, max_col_len)

                    if colname in self.container:
                        self.container[colname].append(value)
                    else:
                        self.container[colname] = [value]

                inp = (input(msg).strip()).lower()

                if inp == 'y' or inp == 'yes':
                    rowno += 1
                    print(hashes)
                    continue # To continue with entering data for next row
                else:
                    # This is just to make the code meaningful even break can also be used
                    nmtc = no_or_mistakenly_typed_confirmation = input("Is this mistakenly typed (y/n): ").strip()

                    if(nmtc.lower() == "n" or nmtc.lower() == "no"):
                        satisfied = True
                    elif not(nmtc.lower() == 'y' or nmtc.lower() == 'yes'):
                        warning("This is for your help, just type proper value to exit/continue")
                    else:
                        rowno += 1

                    print(hashes) 

            self.__states["set_container"] = True
            return True  # Success
        else:
            return False # Failure


    def set_column_names(self):
        """
        Description
        ===========
            - Asks user to enter the name of columns that will appear in csv 
              or (as keys in json object) 
        """
        if self.__states.get('start', None):
            cols = self.total_columns # To short the name (value of cols >= 1)
            
            d = {
                1: '1st',
                2: '2nd',
                3: '3rd'
            }

            f = str(len(str(cols)) + 2) # cols => Total number of columns (extra 2 is for st, nd, rd, th etc.)
            s = "Enter the name of %s column: " % ("%-" + f + "s")
            
            i = 1
            while i <= cols:
                if i <= 3:
                    colname = input(s % (d[i]))
                else:
                    colname = input(s % (str(i) + 'th'))

                if not(re.match(r"^\w*(\w+[-_])*\w+$", colname)):
                    warning("Please do not use characters for column names other than "
                            "A-Za-z0-9_-")
                    continue

                if colname in self.columns:
                    warning('The entered column name {} has been already choosen '
                           '(please enter another name)'.format(colname))
                    continue

                self.columns.append(colname)
                self.collens.append(len(colname)) 
                i += 1

            self.__states["set_column_names"] = True
            return True # Success
        else:
            warning("You are directly trying to invoke, set_column_names() method"
                    ", please call start() method first")
            return False # Failure


    def start(self):
        """
        Description
        ===========
            - Initiates the process of creating dataset, asks for number of columns
            - Valiates entered value (no. of columns), checks if that is a positive 
              integer
            - Checks if it is >= 1
            - Continues to ask user to enter proper value if it does not satisfy the 
              requirement
        """     

        everything_is_ok = False

        while not everything_is_ok:
            cols = input('Enter number of columns that you want in your dataset: ').strip(); 

            if re.match(r"^\d+$", cols):
                cols = int(cols)

                if cols == 0:
                    warning("You are looking for 0 column names, please enter >= 1")
                    continue

                everything_is_ok = True
            else:
                warning("The entered value doesn't look like a +ve integer "
                    "please enter a valid integer number")

        self.total_columns = cols
        self.__states = {"start": True}

        # Do not need to add \n either at beginning or end while calling messages
        # function like success() / warning() / error() etc.
        success("You are successfully done with no. of columns") 

        ret = self.set_column_names()
        if ret:
            success("You are successfully done with the column names")
        else:
            error("Something unexpected happened")

        ret = self.set_container()
        if ret:
            success("You are successfully done with entering data for your dataset")
        else:
            error("Something unexpected happened")

    def status_is_ok(self):
        states = self.__states

        if states["start"]:
            if states["set_column_names"]:
                if states["set_container"]:
                    return True
                else:
                    warning("You are directly trying to invoke, view() method"
                        ", please call start() => set_column_names() => set_container() methods first")
            else:
                warning("You are directly trying to invoke, view() method"
                    ", please call start() => set_column_names() methods first")
        else:
            warning("You are directly trying to invoke, view() method"
                ", please call start() method first")

        return False # Failure

    def view(self):
        """
        Description
        ===========
            - Shows the entered data as a pandas DataFrame
              by using the data contained in class attribute 'container'

            - The 'container' which is a dictionary can be directly accessed via the class
              instance as below:
              
            >>> kd = KaggleDataSetCreator()
            >>> kd.start() 
            >>> kd.container
        """

        if self.status_is_ok():
            self.df = pd.DataFrame(self.container)
            data(self.df) # Success, printing data on Terminal
            return True

        return False

    @property
    def data(self):
        """
        Description
        ===========
            - Returns pandas.DataFrame object created using 'container' 
              dictionary

            - Returns False if the status is not ok i.e. if you failed to call start(),
              and other methods like set_column_names() etc. (Please check documentation
              for more details)
        """

        if self.status_is_ok():
            return self.df 
        else:
            return False


    def to_csv(self, index=True):
        """
        Description
        ===========
            - Creates csv/json file containing the entered data from Terminal
            - Uses the value of attribute named 'container' for creating DataFrame
        """

        csv_path = os.path.join(self.filedir, self.filename + '.' + self.extension)
        self.df.to_csv(csv_path, index=index)
