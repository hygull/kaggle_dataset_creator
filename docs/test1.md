```console
Enter number of columns that you want in your dataset: 2

SUCCESS: You are successfully done with no. of columns
Enter the name of 1st column: fullname
Enter the name of 2nd column: age

SUCCESS: You are successfully done with the column names
[DATA ENTRY] <row 1>  fullname    : Rishikesh
[DATA ENTRY] <row 1>  age         : 26

=======================================
Do you want to add 1 more row (y/n): y
=======================================
[DATA ENTRY] <row 2>  fullname    : Hemkesh
[DATA ENTRY] <row 2>  age         : 27

=======================================
Do you want to add 1 more row (y/n): Malinikesh
Is this mistakenly typed (y/n): y
=======================================
[DATA ENTRY] <row 3>  fullname    : Malinikesh Agrawani
[DATA ENTRY] <row 3>  age         : 34

=======================================
Do you want to add 1 more row (y/n): n
Is this mistakenly typed (y/n): n
=======================================

SUCCESS: You are successfully done with entering data for your dataset
['fullname', 'age']
{'fullname': ['Rishikesh', 'Hemkesh', 'Malinikesh Agrawani'], 'age': ['26', '27', '34']}


              fullname age
0            Rishikesh  26
1              Hemkesh  27
2  Malinikesh Agrawani  34
```