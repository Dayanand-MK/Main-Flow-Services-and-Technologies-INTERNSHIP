# DEVELOP A SIMPLE PYTHON SCRIPT TO SCRAPE DATA FROM A STATIC WEB PAGE

import requests as r
from bs4 import BeautifulSoup as b

url = 'https://www.intel.com/content/www/us/en/homepage.html'

res = r.get(url)

if res.status_code == 200:
    soup = b(res.content, 'html.parser')
    
    headers = soup.get_text()
    
    print(headers)
else:
    print(f'Failed to retrieve the web page. Status code: {res.status_code}')
