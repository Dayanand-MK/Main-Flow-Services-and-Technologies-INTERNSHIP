# EXTRACT RELEVANT INFORMATION SUCH AS TEXT, LINKS, OR IMAGES FROM WEBPAGES

import requests as r
from bs4 import BeautifulSoup as b

url = "https://www.intel.com/content/www/us/en/homepage.html"

res = r.get(url)
if res.status_code == 200:
    so = b(res.text,"html.parser")
    txt = so.get_text()
    lin = [a['href'] for a in so.find_all('a',href = True)]
    img = [i['src'] for i in so.find_all('i',src = True)]

    print("\nTEXT CONTENT\n")
    print(txt)
    print("\nLINKS\n")
    for link in lin:
        print(link)
    print("\nIMAGES\n")
    for image in img:
        print(image)

else:
    print(f'Failed to retrieve the web page. Status code: {res.status_code}')