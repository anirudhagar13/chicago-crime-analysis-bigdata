# bigdata
Version controlling for Big Data

# AWS instance
ec2-54-174-211-0.compute-1.amazonaws.com

# Installation of virtual environment:
- Install virtual environment: `python3 -m pip install --user virtualenv`
- Creation of virtual environment: `python3 -m venv env`
- Activating virtual environment: `source env/bin/activate`
- Installing all dependencies: `pip install -r requirements.txt`

# Instructions to run:
- To run data pipeline: 
- python run.py '../../../../Downloads/Crimes_-_2001_to_present.csv' 'admin' 'password' 'localhost' 'crime_data'
- To answer business analytics questions: 
- python run.py '../../../../Downloads/Crimes_-_2001_to_present.csv' 'admin' 'password' 'localhost' 'crime_data' 1
-

# Buiness requirements:
- (1) Time series data analysis
- (2) Arrest analysis