import requests

url = 'http://127.0.0.1:8000/hello/'
headers = {'Authorization': 'Token 9a3faecbe7a754de5866d11eeeaf893f55aaa991'}
response = requests.get(url, headers=headers)
print('Response from server: ' + str(response.json()))
