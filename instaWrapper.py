import requests

user = input("Type the username: ")
profile_url = f'https://www.instagram.com/{user}/?next=%2F'
followers_url = f'https://www.instagram.com/{user}/followers/?next=%2F'


data = requests.get(followers_url)
print(data.text)