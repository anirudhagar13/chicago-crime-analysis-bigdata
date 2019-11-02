# bigdata
Version controlling for Big Data

# AWS instance
34.229.250.146:8091

# Installation of virtual environment:
- Install virtual environment: `python3 -m pip install --user virtualenv`
- Creation of virtual environment: `python3 -m venv env`
- Activating virtual environment: `source env/bin/activate`
- Installing all dependencies: `pip install -r requirements.txt`

# Instructions to run (Assuming above environment is setup) [All credentials in writeup]:
- To run data pipeline: 
- python run.py 'path_to_data_file' 'username' 'password' 'hostname' 'bucket_name'

- To answer business analytics questions: 
- python run.py 'path_to_data_file' 'username' 'password' 'hostname' 'bucket_name' bq_id
- (analytics functional with csv data dump)

# Buiness questions visualization:
- (1) Time series data analysis
- (2) Arrest analysis
- (3) Crimes reported per year
- (4) Crime with maximum arrests
- (5) Crime distribution by year
- (6) Finding Unsafe neighborhood
- (7) Crime type prediction