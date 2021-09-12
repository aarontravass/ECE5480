import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
myres = requests.get("https://www.orionscache.com/books", headers=headers)
soup = BeautifulSoup(myres.text, "html.parser")
links = soup.find_all('a')
for link in links[:10]:
    print(link.get('href'))
