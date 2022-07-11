from bs4 import BeautifulSoup
import requests

proxies =   {
                'https': 'https://YOURPROXY', 
                'http': 'http://YOURPROXY'
            }
page = requests.get("https://BLOCKEDSITE", proxies=proxies)
soup = BeautifulSoup(page.content, "html5lib")
print(page.text)
