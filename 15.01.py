import requests


api_url = "https://api.github.com/repos/psf/requests"
response = requests.get(api_url)
print('Response status code:', response.status_code)
print('Response body:', response.json())
