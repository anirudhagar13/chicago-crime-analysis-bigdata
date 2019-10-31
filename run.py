'''
Module to run data pipeline
'''
import sys
import datetime
import pandas as pd
from analytics import *
from ingestion import data_ingestion
from manipulation import data_cleansing, data_extraction

def data_load(file_path):
	'''
	Loading data from file
	'''
	# Loading data from csv file dump
	start_time = datetime.datetime.now()
	data = pd.read_csv(file_path)
	end_time = datetime.datetime.now()
	print ('Data Acquisition: ', (end_time - start_time).total_seconds()) 

	return data

def pipeline(csv_dump_path, cb_user, cb_pwd, cb_host, cb_bucket):
	'''
	Module to run data pipeline
	'''
	# Getting data from file
	crime_data = data_load(csv_dump_path)

	# Cleansing data
	start_time = datetime.datetime.now()
	cleansed_data = data_cleansing(crime_data)
	end_time = datetime.datetime.now()
	print ('Data Cleansing: ', (end_time - start_time).total_seconds())

	# Data tranformation to fit model
	start_time = datetime.datetime.now()
	extracted_data = data_extraction(cleansed_data)
	end_time = datetime.datetime.now()
	print ('Data Extraction: ', (end_time - start_time).total_seconds())

	# Data ingestion into couchbase
	start_time = datetime.datetime.now()
	data_ingestion(extracted_data, cb_user, cb_pwd, cb_host, cb_bucket)
	end_time = datetime.datetime.now()
	print ('Data Ingestion: ', (end_time - start_time).total_seconds())

def data_analysis(csv_dump_path, bq_id):
	'''
	Perform analytics depending on business question
	'''
	# Getting data from file as of now
	crime_data = data_load(csv_dump_path)

	if bq_id == '1':
		time_data_analysis(crime_data)
	elif bq_id == '2':
		arrest_analysis(crime_data)
	else:
		print ('Unknown business question ID.')

if __name__ == '__main__':
	# Getting csv dump file path from command line arguments
	try:
		csv_dump_path = sys.argv[1]
		cb_user = sys.argv[2]
		cb_pwd = sys.argv[3]
		cb_host = sys.argv[4]
		cb_bucket = sys.argv[5]

		if len(sys.argv) == 6:
			pipeline(csv_dump_path, cb_user, cb_pwd, cb_host, cb_bucket)
		elif len(sys.argv) == 7:
			bq_id = sys.argv[6]
			data_analysis(csv_dump_path, bq_id)
		else:
			print ('Invalid no of system arguments')
					
	except Exception as e:
		print ('Insufficient parameters to run data pipeline.', e)
