import requests 

# This function sends an HTTP GET request to the specified URL with a timeout of 3 seconds for connection and 5 seconds for reading.
# if within duration boundaries, return the response content 
# otherwise beyond 5 seconds will return timeout
# otherwise on request exception, return the error message  
try:
    response =  requests.get('https://example.com', timeout = (3, 5))
    print(response.content)
except requests.Timeout:
    print("The request timed out")
except requests.RequestException as error:
    print(f"An error occured: {error}")