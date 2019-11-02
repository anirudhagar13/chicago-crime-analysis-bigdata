'''
Specific modules to answer business questions
'''
import numpy as np
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

def time_data_analysis(analysis_df):
	'''
	aggregates and plots data of crime over years
	'''
	# Extracting year from date column
	analysis_df['Year'] = analysis_df['Date'].map(
							lambda x: x.split()[0].split('/')[2])
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
	analysis_df.groupby(['Primary Type', 'Arrest']).size().unstack().plot(
						kind='barh', stacked=True, figsize=(10,10))
	plt.show()

def count_per_year_analysis(analysis_df):
	'''
	number of crime cases reported by year
	'''
	color = cm.magma_r(np.linspace(.2,1.0, 20))
	analysis_df.groupby(['Year']).count()['ID'].plot(kind='barh', 
						figsize=(10,10),color=color)
	plt.show()
    
def max_arrests(analysis_df):
	'''
	crime type with maximum arrests
	'''
	data = analysis_df.groupby(['Primary Type']).count()['ID'].idxmax()
	print ('Crime type with Maximum arrests: ', data)

def crime_distribution_by_year(analysis_df):
	'''
	crime type with maximum arrests
	'''
	crime_types = analysis_df['Primary Type'].unique()
	analysis_df.groupby(['Primary Type']).count()['ID'].idxmax();
	ax = plt.gca()
	year_group = analysis_df.groupby(['Year', 
				'Primary Type'])['Year'].count().unstack('Primary Type').fillna(0)
	year_group[crime_types].plot(kind = 'bar', stacked = True,figsize=(10,10),
									ax=ax);
	ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
	plt.show();
    
def unsafe_neighbourhood(analysis_df):
	'''
	returns the most unsafe neighbourhood
	'''
	data = analysis_df.groupby(['Neighbourhood']).count()['Primary Type'].idxmax()
	print ('Most unsafe Neighbourhood in Chicago: ', data)

def crime_type_prediction(analysis_df, predict_loc):
	'''
	Trains and predicts crime type, based on location given as one-hot encoding
	'''
	df_crime = analysis_df['Primary Type']
	y = analysis_df['Location Description']
	df1 = pd.get_dummies(df_crime).head(200)
	X = df1.as_matrix()
	clf = LogisticRegression(random_state=0, solver='lbfgs', 
								multi_class='multinomial').fit(X, y.head(200))
	y_test=clf.predict(predict_loc)
	print ('Predicted Location: ', y_test)

