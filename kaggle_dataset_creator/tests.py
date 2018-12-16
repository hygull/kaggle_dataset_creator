from kaggle_dataset_creator import KaggleDataSetCreator

def test_filename_extension_filedir():
	# TEST CASE 1
	kaggle_dataset = kd = KaggleDataSetCreator()

	print(kd.filename)
	print(kd.filedir)
	print(kd.extension)
	print()
	# KaggleDataSet
	# .
	# csv


	# TEST CASE 2
	kaggle_dataset2 = kd2 = KaggleDataSetCreator(
								path = 'MyOwnFile', 
								extension = "json"
							)

	print(kd2.filename)
	print(kd2.filedir)
	print(kd2.extension)
	print()
	# MyOwnFile
	# .
	# json


	# TEST CASE 3 (Correct path is provided, file name with extension, externally provided extension {skipped})
	kaggle_dataset3 = kd3 = KaggleDataSetCreator(
								path = 'C:\\Users\\MyOwnFile.csv', 
								extension="json"
							)

	print(kd3.filename)
	print(kd3.filedir)
	print(kd3.extension)
	print()
	# MyOwnFile
	# C:\Users
	# csv


	# TEST CASE 4 (Wrong path is provided)
	kaggle_dataset4 = kd4 = KaggleDataSetCreator(
								path = 'C:\\Use\\MyOwnFile2.csv', 
								extension="json"
							)

	print(kd4.filename)
	print(kd4.filedir)
	print(kd4.extension)
	print()
	# MyOwnFile2
	# .
	# csv


	# TEST CASE 5 (MyDataSet already exists in current directory)
	kaggle_dataset5 = kd5 = KaggleDataSetCreator(path = 'MyDataSet1.csv')

	print(kd5.filename)
	print(kd5.filedir)
	print(kd5.extension)
	print()
	# MyDataSet1-1.csv
	# .
	# csv

test_filename_extension_filedir()





