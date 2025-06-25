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
        self.jobQueue.put(self.seedURL)
        self.visitedURLs.add(self.seedURL)
        print(f'initialized queue with seed URL: {self.seedURL}')


    def startScraping(self, domain):
        crawlerInstance = crawler.Crawler(domain)
        while not self.jobQueue.empty():
            currentURL = self.jobQueue.get()
            foundURLs = crawlerInstance.scrape(currentURL)
            for link in set(foundURLs):
                if urllib.parse.urlparse(link).netloc == domain and link not in self.visitedURLs:
                    self.jobQueue.put(link)
                    self.visitedURLs.add(link)
            self.URLmap[currentURL] = foundURLs
        return self.URLmap
                