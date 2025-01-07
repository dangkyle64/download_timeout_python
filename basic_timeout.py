import requests 

# This function sends an HTTP GET request to the specified URL with a timeout of 5 seconds.
# if within 5 seconds, return the response content 
# otherwise beyond 5 seconds will return timeout 
try:
    response =  requests.get('https://example.com', timeout = 5)
    print(response.content)
except requests.Timeout:
    print("The request timed out")