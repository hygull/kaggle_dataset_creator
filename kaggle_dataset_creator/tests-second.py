from kaggle_dataset_creator import KaggleDataSet

kd = KaggleDataSet()
kd.start()

print(kd.columns)
print(kd.container)

kd.view();   # To view the final DataFrame on Terminal
kd.to_csv(); # To save in csv, default file name is take if filename is not provided 

print("DATA:- ")
print(kd.dataset) # Accessing dataset attribute to get the final DataFrame

print('Total rows: ', kd.rows)
print('Types', kd.data_types)
