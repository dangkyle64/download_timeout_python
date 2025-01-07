import requests 
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry 

# create retry object for adapter to use on the next 5 failed downloads
retry = Retry(total = 5, backoff_factor = 1, status_forcelist = [500, 502, 503, 504])
adapter =  HTTPAdapter(max_retries = retry)

# create session object to mount the HTTP get request to the requested link using the adapter properties 
session = requests.Session()
session.mount('http://', adapter)
session.mount('https://', adapter)

# This function sends an HTTP GET request to the specified URL with a timeout of 3 seconds for connection and 5 seconds for reading.
# if within duration boundaries, return the response content 
# otherwise beyond 5 seconds will return timeout
try:
    response = session.get('https://example.com', timeout = (3, 5))
    print(response.content)
except requests.Timeout:
    print("The request timed out")