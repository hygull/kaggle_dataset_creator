
import os
import re
import pandas as pd
from messages import warning, success


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
            filename = filename + "-" + str(i) + '.' + extension;
            i = i + 1;

        return filedir, filename, extension


    def get_column_names(self):
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

                if not(re.match(r"^\w+(\w+[-_])*\w+$", colname)):
                    warning("Please do not use characters for column names other than "
                            "A-Za-z0-9_-")
                    continue

                if colname in self.columns:
                    warning('The entered column name {} has been already choosen '
                           '(please enter another name)'.format(colname))
                    continue

                self.columns.append(colname)
                i += 1
        else:
            return self.columns


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
        # function like success() / warning() etc.
        success("You are successfully done with no. of columns") 

        columns = self.get_column_names()
        success("You are successfully done with the column names")


    def create_csv(self):
        """
        Description
        ===========
            - Creates csv/json file containing the entered data from Terminal
        """

        df = pd.DataFrame(self.container, columns=self.columns)
        csv_path = os.path.join(self.filedir, self.filename, self.extension)

        pd.to_csv(csv_path)


