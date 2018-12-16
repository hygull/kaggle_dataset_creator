"""
	Created on: 16 Dec 2018
	Aim: To produce dataset to publish on Kaggle (or for simple use as csvs, json etc.)
"""

import os
import re
import pandas as pd
from messages import warning


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

		# Repeatedly check for an existance of specified filename, 
		# if it already exists (do not override)
		# and choose another file name by appending numbers like 1, 2, 3 and so...on
		i = 1
		while os.path.exists(os.path.join(filedir, filename + '.' + extension)):
			filename = filename + str(i) + '.' + extension
			i = i + 1;

		return filedir, filename, extension


	def start(self):
		pass

	def create_csv(self):
		pass

