
import requests

def getPageRequests(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    result = requests.get(url)
    file = open('FILE.txt', 'w')
    file.write(result.text)
    file.close()
url=input("Enter a url = ")
getPageRequests(url)
