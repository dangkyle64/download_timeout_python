# Download Timeout Example with Possible Solution

Python scripts displaying some timeout on HTTP request examples. Also displays usage of the requests and urllib3 libraries to retry the GET requests after certain connection and read durations. 

## Table of Contents
- [Installation](#installation)
- [Requirements](#requirements)
- [Install Dependencies](#install-dependencies)
- [Usage](#usage)


## Installation

Clone the repository:
   ```bash
   git clone https://github.com/dangkyle64/download_timeout_python
   ```

### Requirements
- Python 3.x
- requests 2.*
- urllib3 2.3.*

### Install Dependencies

```bash
# Install required dependencies
pip install -r requirements.txt
```

### Usage

Basic requests library usage where timeout for both connection and read time are int1
```python
import requests

try:
   response = requests.get('url-link-to-download-from', timeout = int1)
   print(response.content)
except requests.Timeout:
    print("The request timed out")
```

Requests library usage where timeout tuple is used where connection is int1 and read time is int2
```python
import requests

try:
   response = requests.get('url-link-to-download-from', timeout = (int1, int2))
   print(response.content)
except requests.Timeout:
    print("The request timed out")
   
```

Urllib3 retry usage to set up retry properties
- total is for retry attempts
- backoff_factor is for increasing time between each retry 
- status_forcelist is for specific errors that will force the retry ex. status code 500
```python

from urllib3.util.retry import Retry 

retry = Retry(total = int, backoff_factor = int, status_forcelist = [])
```