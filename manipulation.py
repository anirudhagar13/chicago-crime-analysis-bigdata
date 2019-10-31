'''
Modules to manipulate data
'''
import numpy as np
import pandas as pd

def null_trim(df):
	'''
	Finding and removing null data
	'''
	# hardcoded columns to look for null values
	focus_columns = ['date','primary_type','arrest','location']

	new_df = df.dropna(subset=focus_columns)
	print ('No of null values dropped:', df.shape[0] - new_df.shape[0])
	return new_df

def col_name_const(df):
	'''
	Renaming columns to a consistent format
	'''
	df.columns = [x.replace(' ','_').lower() for x in df.columns]
	return df

def date_time_conv(df):
	'''
	parses data and converts to epoch
	'''
	# Extremely intensive function, find alternative
	if 'date' in df.columns:
		df['date'] = pd.to_datetime(df['date'])

	return df

def data_cleansing(df):
	'''
	Cleanses and tranforms data
	'''
	df = col_name_const(df)
	df = null_trim(df)
	return df

def data_extraction(df):
	'''
	Converts data into 
	'''
	# Use rest client to get location data

	# Hardcoded data model for data extraction
	data_model = ['Crime_Type','Location','Date','Loc_desc',
				'Latitude','Longitude','Arrest','Beat','Year']

	filter_cols = list()
	for col in data_model:
		if col.lower() in df.columns:
			filter_cols.append(col.lower())

	# Rest function logic comes here
	return df[filter_cols]
