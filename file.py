import requests
api_url = 'https://api.breakingbadquotes.xyz/v1/quotes'
print(api_url)
response = requests.get(api_url)
print(response.json())
