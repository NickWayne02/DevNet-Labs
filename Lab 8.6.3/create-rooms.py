import requests

access_token = 'YjJhOTQ2NTUtNjRlOS00YzBjLWExMmMtM2IwZTQ1NTRlNzgyN2UyN2Y3YjEtNjA0_P0A1_42801c13-223b-4359-9cea-9fc396422e33'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
