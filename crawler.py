import requests
from bs4 import BeautifulSoup
import urllib.parse 



class Crawler:
    """
    A web crawler that scrapes a given URL and returns a list of URLs found on that page. Kept separate to allow for possible multithreading in future.
    """

    def __init__(self, domain, failoverAction):
        self.domain = domain
        self.failoverAction = failoverAction

    def scrape(self, url):
            """
            Scrapes the given URL and returns a list of the URLs found as a list.
            If the URL request fails, it either passes out an empty list to allow the crawler to continue or raises an error and terminates the program
            """
            #get the URL
            try:
                rawPage = requests.get(url)
            except requests.RequestException as e:
                 print(f"Unable to fetch URL {url}: {e}")
                 if self.failoverAction == 'continue':
                      print(f"skipping to next URL, current URL returned error")
                      return []
                 elif self.failoverAction == 'stop':
                      print(f'terminating due to errror')
                      raise
            #parse the page and find all the links on the page
            soup = BeautifulSoup(rawPage.text, 'html')
            foundURLs = [urllib.parse.urljoin(f'https://{self.domain}', link['href']) for link in soup.find_all('a', href=True)]
            #print out the base URL and URLs present on the base URL's page
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