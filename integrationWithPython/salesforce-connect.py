import requests

authorization_endpoint = 'https://login.salesforce.com/services/oauth2/authorize'
token_endpoint = 'https://login.salesforce.com/services/oauth2/token'
client_id = '<CLIENT_ID>'
client_secret = '<CLIENT_SECRET>'
redirect_uri = '<REDIRECT_URI>'
scopes = '<scopes>'

# make a get request to get auth code 
auth_code_url = authorization_endpoint+'?response_type=code&client_id='+client_id+'&redirect_uri='+redirect_uri+'&scopes='+scopes
print(auth_code_url)

auth_code ='<auth_code>'
# make post request to get access token 

response = requests.post(token_endpoint,data={

    'client_id':client_id,
    'client_secret':client_secret,
    'grant_type':'authorization_code',
    'redirect_uri':redirect_uri,
    'code':auth_code

})

response = response.json()

access_token = response['access_token']
instance_url = response['instance_url']

url = instance_url +'<api_url>'
res = requests.post(url,headers={'Authorization': 'Bearer '+access_token,'Content-Type':'application/json'})
print(res.json())