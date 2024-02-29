import requests
from bs4 import BeautifulSoup


url = 'https://infopark.in/companies/company/thrissur'
response = requests.get(url,verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

h3_tags = soup.find_all('h3')
for tag in h3_tags:
    print(tag.text)
