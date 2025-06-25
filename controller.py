from queue import Queue
import crawler
import re
import urllib.parse

class Controller:

    def __init__(self, domain, seedURL):
        self.domain = domain
        self.seedURL = seedURL
        self.jobQueue = Queue()
        self.visitedURLs = set()
        self.URLmap = {}

    def setupController(self):
        standardizedURL = self.standardizeURL(self.seedURL)
        self.jobQueue.put(standardizedURL)
        self.visitedURLs.add(standardizedURL)
        print(f'initialized queue with seed URL: {standardizedURL}')


    def startScraping(self, domain):
        crawlerInstance = crawler.Crawler(domain)
        while not self.jobQueue.empty():
            currentURL = self.jobQueue.get()
            foundURLs = crawlerInstance.scrape(currentURL)
            for link in set(foundURLs):
                standardizedLink = self.standardizeURL(link)
                if urllib.parse.urlparse(standardizedLink).netloc == domain and standardizedLink not in self.visitedURLs:
                    self.jobQueue.put(standardizedLink)
                    self.visitedURLs.add(standardizedLink)
            self.URLmap[currentURL] = foundURLs
        return self.URLmap
    
    @staticmethod
    def standardizeURL(url):
        parsedURL = urllib.parse.urlparse(url)
        netloc = parsedURL.netloc
        path = parsedURL.path.rstrip('/')
        query = urllib.parse.urlencode(sorted(urllib.parse.parse_qsl(parsedURL.query)))
        return urllib.parse.urlunparse((parsedURL.scheme, netloc, path, '', query, ''))