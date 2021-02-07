import requests


url = 'https://habr.com/ru/post/409915/'


req = requests.get(url)

print(req.text)