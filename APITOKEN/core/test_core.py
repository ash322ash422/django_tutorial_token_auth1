import requests, json

#Following code retrieves the token for a user.
url = 'http://127.0.0.1:8000/api-token-auth/'
response = requests.post(url,data={'username': 'admin', 'password': 'admin'})
print('Response from server: ' + str(response.json()))
response_dict = json.loads(response.text)
print('token=',response_dict['token'])
print("#############################")


url = 'http://127.0.0.1:8000/hello/'
#NOTE I could have retrieved token from above and used it below. 
headers = {'Authorization': 'Token 9a3faecbe7a754de5866d11eeeaf893f55aaa991'}
response = requests.get(url, headers=headers)
print('Response from server: ' + str(response.json()))

