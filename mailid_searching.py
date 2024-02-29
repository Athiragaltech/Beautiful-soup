import re
import requests
from bs4 import BeautifulSoup


url = "https://infopark.in/companies/company"
r = requests.get(url, verify=False)
soup = BeautifulSoup(r.content, 'html.parser')
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
all_text = soup.get_text()
email_addresses = re.findall(email_pattern, all_text)
for email in email_addresses:
    print(email)

#company names
h3_tags = soup.find_all('h3')
for tag in h3_tags:
    print(tag.text)

#address
p_tags = soup.find_all('p')
for tag in p_tags:
    print(tag.text)




















driver.close()
