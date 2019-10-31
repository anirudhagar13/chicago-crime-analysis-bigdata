'''
Modules to perform data ingestion
'''
import threading
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator

def push_data(data, cb_conn, thread_id):
    '''
    Push data using parallel threads
    '''
    # Creating key using thread name
    bulk_data = dict()
    for index, doc in enumerate(data):
        doc_id = 'k' + str(index) + '_' + thread_id
        bulk_data[doc_id] = doc
        
    try:
    	# Bulk uploading of documents
        cb_conn.upsert_multi(bulk_data)
    except:
        print ('Data Insertion failed!')
        
    print ('Thread completed ingestion: ', thread_id)

def sequential_run(cb_conn, data):
	'''
	Pushes data sequentially
	'''
	bulk_data = dict()

	for index, doc in enumerate(data.T.to_dict().values()):
	    doc_id = 'k' + str(index)
	    bulk_data[doc_id] = doc
	    
	# API for bulk ingestion
	cb_conn.upsert_multi(bulk_data)

def parallel_run(cb_conn, data, threads=10):
	'''
	Pushes data parallely
	'''
	jobs = list()

	# Hardcoded chunk of data by each thread
	chunk_size = 1000
	
	for i in range(0, threads):
	    chunk = data[chunk_size*i:chunk_size*(i+1)].T.to_dict().values()
	    thread = threading.Thread(target=push_data(chunk, cb_conn, str(i+1)))
	    jobs.append(thread)

	# Start the threads (i.e. calculate the random number lists)
	for j in jobs:
	    j.start()

	# Ensure all of the threads have finished
	for j in jobs:
	    j.join()

def data_ingestion(data, cb_user, cb_pwd, cb_host, cb_bucket):
	'''
	Ingests data into pipeline
	'''
	cluster = Cluster('couchbase://' + cb_host)
	authenticator = PasswordAuthenticator(cb_user, cb_pwd)
	cluster.authenticate(authenticator)
	cb_conn = cluster.open_bucket(cb_bucket)

	# Pushing entire data sequentially
	# sequential_run(cb_conn, data)

	# Pushing entire data parallely
	parallel_run(cb_conn, data)
