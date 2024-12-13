import requests


r = requests.get('https://api.chucknorris.io/jokes/random')
print(r.json())
print(r.json()["value"])
# print(r.status_code)

# r.headers['content-type']
#
# r.encoding
#
# r.text
#
# r.json()