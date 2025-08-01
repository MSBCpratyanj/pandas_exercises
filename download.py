import pandas as pd
import requests
from io import StringIO

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
response = requests.get(url,verify=False)
print(f"Downloading data from {url}...")
print(f"Status code: {response.status_code}")
# Check if the request was successful
if response.status_code == 200:
    users = pd.read_csv(StringIO(response.text), sep='|', index_col='user_id')
    users.to_csv("user.csv")
    print("Data loaded successfully!")
else:
    print(f"Failed to download data. Status code: {response.status_code}")