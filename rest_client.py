# REST API Client
import requests

class API_client:
    def __init__(self, url, username, password):
        self._url = url
        self._auth = (username, password)
        
    def set_url(self, url):
        '''
        to reset url
        '''
        self._url = url
        
    def get_response(self):
        '''
        get response from url
        '''
        resp = requests.get(self._url, auth=self._auth)
        
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET rest API issue: {}'.format(resp.status_code))
            
        return resp.json()
    
    def put_response(self, data):
        '''
        put response
        '''
        resp = requests.post(self._url, auth=self._auth, json=data)
        
        if resp.status_code != 201:
            raise ApiError('POST rest API issue: {}'.format(resp.status_code))
            
        return 'POST successful'
        
    def __str__(self):
        return 'This is a REST API functions wrapper'

if __name__ == '__main__':
    # Code to test above class
    host_name = 'http://localhost:8091'
    url = '/pools/default/buckets'

    # Instantiating rest client class
    rest_client = API_client(host_name+url, 'admin', 'password')

    # Getting response
    print (rest_client.get_response())
