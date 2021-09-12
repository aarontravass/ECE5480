import requests
from bs4 import BeautifulSoup
import webbrowser
import sys

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}

print("Searching for " + "+".join(sys.argv[1:]))
myres = requests.get("https://scholar.google.com/scholar?hl=en&q=" + "+".join(sys.argv[1:]) + "&*", headers=headers)
soup = BeautifulSoup(myres.text, "html.parser")
elems = soup.select(".gs_rt a")
num = min(len(elems), 5)
for i in range(num):
    url=elems[i].get("href")
    print(url)
    webbrowser.open_new_tab(url)
