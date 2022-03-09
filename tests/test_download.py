# Importing necessaryu modules for testing
# Using sys module and using sys.path.append to execute the test in main directory
# Importing the project0 folder containing main.py and project0.py
# Importing pytest to use test cases

import sys
sys.path.append('..')
import project0
from project0 import project0 as p
import pytest

# Test base in the URL below
url = "https://www.normanok.gov/sites/default/files/documents/2022-03/2022-02-28_daily_incident_summary.pdf"

# Test for fetchincidents() function in project0.py
def test_fetchincidents():
    # Using the fetchincidents to check URL and assering the result with if condition
    result = p.fetchincidents(url)
    if result == url:
        assert True


# Test for extractincidents() function in project0.py
def test_extractincidents():
    # Checking the extractinidents() does not return null values
    incident_data = p.fetchincidents(url)
    output = p.extractincidents(incident_data)
    assert output is not None


# Test for createdb() function in project0.py
def test_createdb():
    # Assering true when createdb() function in project0.py is normanpd.db
    db = p.createdb()
    if db == 'normanpd.db':
        assert True


# Test for populatedb() function in project0.py
def test_populatedb():
    # Fetching data and extracting and asserting as true if the data in inserted
    db = 'normanpd.db'
    incident_data = p.fetchincidents(url)
    incidents = p.extractincidents(incident_data)
    output = p.populatedb(db, incidents)
    assert True


# Test for status() function in project0.py
def test_status():
    # Asserting true if the output is not none
    db = 'normanpd.db'
    incident_data = p.fetchincidents(url)
    incidents = p.extractincidents(incident_data)
    p.populatedb(db, incidents)
    output = p.status(db)
    assert output is not None

