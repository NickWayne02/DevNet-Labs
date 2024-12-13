import requests

access_token = 'YjJhOTQ2NTUtNjRlOS00YzBjLWExMmMtM2IwZTQ1NTRlNzgyN2UyN2Y3YjEtNjA0_P0A1_42801c13-223b-4359-9cea-9fc396422e33'  # Замените на ваш токен
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMjU0ZTFiYjAtYjI2ZC0xMWVmLWI0OTEtNjM0NzMwZWI0YjI5'          # Замените на ID вашей комнаты
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())
