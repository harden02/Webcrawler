import requests
from bs4 import BeautifulSoup
import urllib.parse 
from queue import Queue
import re



class Crawler:

    def __init__(self, domain):
        self.domain = domain

    def scrape(self, url):
            rawPage = requests.get(url)
            soup = BeautifulSoup(rawPage.text, 'html')
            foundURLs = [urllib.parse.urljoin(f'https://{self.domain}', link['href']) for link in soup.find_all('a', href=True)]
            print(f"Base URL is : {url}, found URLs: {foundURLs}")
            return foundURLs
            

            






#rawPage = requests.get('https://monzo.com/')
#soup = BeautifulSoup(rawPage.text, 'html')
#
#visitURLs = Queue()
#foundURLs = set()
#pattern = re.compile(r'^https://monzo.com/')
#
#for link in soup.find_all('a', href=True):
#    abslink = urllib.parse.urljoin("https://monzo.com/", link['href'])
#    #print(f"URL IS:  {abslink}")
#    if pattern.match(abslink) and abslink not in foundURLs:
#        visitURLs.put(abslink)
#    foundURLs.add(abslink)
#print(list(visitURLs.queue))