# Importing necessary libraries to be unsed in this program.
# Module urllib for url in fetchincidents()
# Module PyPDF2 to read and extract data from pdf in extractincidents()
# Module tempfile to store incident data in extractincidents() temporarily
# Module re ( regular expressions ) to replace the new line and format the data with necessary patterns in extractincidents()
# Module sqlite3 for database connections
# Module pandas for processing data into rowns and columns unsing pandas dataframes and then using pandas to insert data into the incidents table using iterrows() method which is in pandas

import urllib.request as urlr
import PyPDF2 as pyp
import tempfile as tf
import re as r
import sqlite3 as sql
import pandas as pd

db='normanpd.db'

def fetchincidents(url):

    #Source - given in project 0 documentation question
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    # Selecting pdf url form normanok.gov
    # url - https://www.normanok.gov/sites/default/files/documents/2022-03/2022-02-28_daily_incident_summary.pdf 
    data = urlr.urlopen(urlr.Request(url, headers=headers)).read()
    # Returning the data to be used by other functions
    return data


def extractincidents(incident_data):
    fp = tf.TemporaryFile()
    fp.write(incident_data)
    fp.seek(0)
    pdfReader = pyp.pdf.PdfFileReader(fp)
    pagecount =  pdfReader.getNumPages()
    # Information given in project 0 documentation question
    pagedata1 = []
    for i in range(1, pagecount):
        pagei = pdfReader.getPage(i).extractText()
        # Source for understanding Regular Expressions - https://docs.python.org/3/library/re.html 
        pagedata = r.sub(' \n', ' ', pagei)
        # Source for understanding re.split() method for finding patterns and using to split accordingly - https://stackoverflow.com/questions/41220172/regex-to-splitstring-on-date-and-keep-it
        pagedata = r.split(r"\s+(?=\d+/\d+/\d+\s)", pagedata)
        for j in pagedata[0:-1]:
            # Splitting the pagedata from 0 to end of data with loop to new line
            pagedata = j.split('\n')
            # Once the criteria of of 5 columns in pagedata is met, we append the data to new variable
            if len(pagedata)==5:
                pagedata1.append(pagedata)
    # Source - using pandas as it is easy to seperate data into columns - https://www.geeksforgeeks.org/python-pandas-dataframe/
    df = pd.DataFrame(pagedata1)
    # Specifying the columns for the dataframe of finaldf
    df.columns = ["incident_time", "incident_number", "incident_location", "nature", "incident_ori"]
    return df 

def createdb():
    #Source - https://docs.python.org/3.8/library/sqlite3.html
    # Naming convension as given in question documentation for database name, table name and table columns
    database_name = 'normanpd.db'
    # Connecting to database
    conn = sql.connect(database_name)
    db = conn.cursor()
    # Table to be droped before creating to eliminate any errors while re executing at a different time
    db.execute(" DROP TABLE IF EXISTS incidents")
    # Create table execute function. SQL command given in question documentation
    db.execute(""" CREATE TABLE incidents
                    (incident_time TEXT,
                    incident_number TEXT,
                    incident_location TEXT,
                    nature TEXT, 
                    incident_ori TEXT);""")
    # Commiting the connection
    conn.commit()
    # Closing the connection
    conn.close()
    return database_name


def populatedb(db, incidents):
    #Source - https://docs.python.org/3.8/library/sqlite3.html
    # Specifying the data created as normanpd.db as in question
    db = 'normanpd.db'
    # Connecting to database
    conn = sql.connect(db)
    db = conn.cursor()
    # Using iterrows() method in pandas to insert dataframe values according to its columns as described in extractdata()
    # Source - https://www.geeksforgeeks.org/python-pandas-dataframe/
    for i, j in incidents.iterrows():
        # Executing the INSERT SQL command
        conn.execute('INSERT INTO incidents VALUES(?,?,?,?,?)', (j['incident_time'], j['incident_number'], j['incident_location'], j['nature'], j['incident_ori']) )
        # Commiting database connection
        conn.commit()
    # Closing database connection    
    conn.close()


def status(db):
    # Specifying the data created as normanpd.db as in question
    db = 'normanpd.db'
    # Connecting to database
    conn = sql.connect(db)
    db = conn.cursor()
    # Executing the SQL command for nature and its count using execute function
    result = db.execute("""SELECT nature ||'|'|| count(nature) FROM incidents
                  GROUP BY nature """).fetchall()
    for nature in result:
        print (nature[0])
        # Printing the results to output screens after processing
    return result
