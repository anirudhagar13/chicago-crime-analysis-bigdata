'''
Modules to manipulate data
'''
import time
import numpy as np
import pandas as pd
from rest_client import API_client

def col_manipulate(df):
	'''
	Renaming some columns to more intuitive names
	'''
	new_df = df.rename(columns={"Primary Type":"Crime_Type", 
								"Case Number": "Case_Number",
								"Location Description":"Location_Description"})
	return new_df

def null_trim(df):
	'''
	Finding and removing null data
	'''
	# hardcoded columns to look for null values
	focus_columns = ['date','crime_type','arrest','location']

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
	df = col_manipulate(df)
	df = col_name_const(df)
	df = null_trim(df)
	return df

def getCountyAndNeighbourhood(lon, lat, apc):
	strr = "https://api.opencagedata.com/geocode/v1/json?key=d3b9224f3e3049788ee8774fd3796d88&q="+str(lon)+'+'+str(lat)
	apc.set_url(strr)
	s = apc.get_response()
	if(len(s['results'])==0):
		return np.nan
	if(s['results'][0]['components'].get('neighbourhood') != None):
		return s['results'][0]['components']['neighbourhood']

def loc_data(df):
	'''
	Uses API client to get location data and adds as new column
	'''
	count = 0
	lc = list()
	lg = df['longitude'].tolist()
	lt = df['latitude'].tolist()
	apc =  API_client("","","")
	
	# Looping and getting neighborhood data one by one
	for i, j in zip(lg, lt):
	    if np.isnan(i) == False and np.isnan(j) == False and count < 2490:
	        time.sleep(1.1)
	        c = getCountyAndNeighbourhood(j, i, apc)
	        lc.append(c)
	        count= count+1
	    else:
	        lc.append(np.nan)

	df['neighbourhood'] = lc

	return df

def data_extraction(df):
	'''
	Converts data into 
	'''
	# Use external API to get new location data
	df = loc_data(df)

	# Hardcoded data model for data extraction
	data_model = ['id','case_number','crime_type','location_description','date',
					'neighbourhood','arrest','beat','year']

	filter_cols = list()
	for col in data_model:
		if col.lower() in df.columns:
			filter_cols.append(col.lower())

	# Rest function logic comes here
	return df[filter_cols]
