'''
Specific modules to answer business questions
'''
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

def time_data_analysis(analysis_df):
	'''
	aggregates and plots data of crime over years
	'''
	# Extracting year from date column
	analysis_df['Year'] = analysis_df['Date'].map(lambda x: x.split()[0].split('/')[2])
	analysis_series = analysis_df.groupby('Primary Type')['Year'].value_counts()

	# Aggregating data on the basis of year
	time_data = dict()
	for index, count in analysis_series.items():
	    p_type = index[0]
	    year = index[1]
	    if p_type not in time_data:
	        time_data[p_type] = [[],[]]
        
	    # Append
	    time_data[p_type][0].append(year)
	    time_data[p_type][1].append(count)

	# Plot a line graph
	for p_type, value in time_data.items():
	    years = value[0]
	    counts = value[1]
	    plt.plot(years, counts, label=p_type)

	# Add labels and title
	plt.title("Time Data Analysis")
	plt.xlabel("X-axis")
	plt.ylabel("Y-axis")

	plt.legend()
	plt.show()

def arrest_analysis(analysis_df):
	'''
	displays no of arrests and non-arrests for each crime type
	'''
	color = cm.inferno_r(np.linspace(.4,.8, 30))
	analysis_df.groupby(['Primary Type', 'Arrest']).size().unstack().plot(kind='barh', stacked=True, figsize=(10,10))
