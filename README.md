**Author - Sanoj Doddapaneni**

**Introduction** – In this project, one of the pdfs of incident data summary report is downloaded from the website of normanok.gov which consists of daily case summaries of incidents according to their nature, date and other information associated to it divided into 5 different columns. This project is developed using Python and Command line tools in Ubuntu.

**Sources** – 
*URL considered - https://www.normanok.gov/sites/default/files/documents/2022-03/2022-02-28_daily_incident_summary.pdf
Sources for Regular Expressions – 
re.sub() – https://docs.python.org/3/library/re.html
re.split() – https://stackoverflow.com/questions/41220172/regex-to-splitstring-on-date-and-keep-it
pandas DataFrame for separating and inserting into the table (incidents) – https://www.geeksforgeeks.org/python-pandas-dataframe/
sqlite3 source and execution – https://docs.python.org/3.8/library/sqlite3.html*

**Installation directions** – We use the packages urllib, PyPDF2, tempfile, re, sqlite3 and pandas where urllib and tempfile packages are inbuilt with python and does not need separate installation and remaining packages can be installed using commands – pipenv install PyPDF2, pipenv install re, pip install sqlite3 and pip install pandas respectively. These packages will be imported into the project when required.

**Project Description** – 

**main.py file** – This file is provided in the directory project0 which consists of the functions of project0.py by importing the project0 directory and its functions and execute then by using command – pipenv run python project0/main.py –incidents #url (followed by URL of PDF without the # symbol).

**project0.py** – This python file consists of functions and their logic to perform necessary operations to print the output as desired. Each function and its uses are explained further accordingly.

Firstly, the packages required are imported which are mentioned in Installation directions.

**fetchincidents(url)** – This function is used to read the data from the url of the pdf using urllib.request package and returns the data into data object which can be used in other functions for further processing.

**extractincidents()** – This function first collects the data from fetchincidents() and then sores it into temporary file which uses tempfile package. Now, the package PyPDF2 package is used to read the pdf pages and its data accordingly. Now, we use the package re (regular expressions) to parse the information collected in the string form using re.sub() and re.split() methods and then, we split the data from 0 to the end of string using loop with new line and use python pandas package DataFrames to specify the data into dataframes and specify their rows according to their columns needed.

**createdb()** – This function is used to create database normanpd.db and then create the table incidents in the database with the columns incident_time, incident_number, incident_location, nature and incident_ori using SQL commands. Firstly, the connection is established to the database using sqlite3 package which has been imported at the beginning and then we execute the drop table command to clean the any previous table created on the name of incidents and then execute create table command accordingly. These SQL commands are executed using execute() method. This only creates the table incidents and does not process or take any actions on the data extracted in extractincidents() function.

**populatedb()** – This function is used to insert our data extracted in extractincidents() into the incidents table created in created(). Here, we normally use loop iteration to insert data into the table using the incidents table columns. As we have used pandas in extract incidents to divide data into DataFrames, we need to use pandas inbuilt method called iterrows in the loop and then specify the columns and then use SQL command to insert data using sqlite3 package execute method.

**status()** – This function is used to print the desired output which is nature of incidents according to its count. We use sqlite3 package to connect to the database using connect method and execute function to execute the SELECT command to retrieve the data from the database and then print it as result using loop for each iteration of nature.

**Test cases** – 

We have created a new directory called tests and then created a file called test_download.py which contains different functions of test cases for each function in project0.py. Each test case in the file is explained below accordingly.

Firstly, we import the packages sys to execute test file for all the directories of the project and provide the path accordingly and then import project0 folder and project0.py within the folder and then finally we should import package pytest to run testcases accordingly. Pyest modules works on pytest framework and can be installed using pipenv install pytest command.

We declare a url which we considered for project0 and write the tests accordingly.

**test_fetchincidents()** – Here, we call the functions fetchincidents() from project0.py and check it with our own url and arrest true accordingly using if statement.

**test_extractincidents()** – In this function, we take output of extractincidents() from project0.py and assert not None.

**test_createdb()** – This function take the db from createdb() function from project0.py and compare it to the db in test case. Using if condition if the createdb() has normanpd.db the test case will be passed.

**test_populatedb()** – Here, we run the popuatedb() function from project0.py and assert true for test case to be passed.

**test_status()** – Here, we check for not None condition of output which calls status() function from project0.py and the test is passed accordingly.

**Possible Bugs** - 

In test_download.py we run test cases for each function considering the URL declared in the test_download.py and the normanpd.db database. Any changes to this database name or URL will result in failed test cases for the test functions. Further, when using pandas, dataFrames should be associated to their columns and same column names should be given in intert SQL command in populatedb() function. It will result in error when the column declaration is removed.

At the end, these files are added, committed and pushed into git hub using git commands accordingly for each file.
