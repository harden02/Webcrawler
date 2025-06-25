from queue import Queue
import crawler
import re
import urllib.parse

class Controller:

    def __init__(self, domain, seedURL):
        self.domain = domain
        self.seedURL = seedURL
        self.jobQueue = Queue()
        self.visitedURLs = {}

    def setupController(self):
        self.jobQueue.put(self.seedURL)
        print(f'initialized queue and visited URLs with seed URL: {self.seedURL}')
        domainlink = "https://" + self.domain
        pattern = fr'^{domainlink}'
        print(f'domain url is {pattern}')
        return pattern


    def startScraping(self, domain):
        crawlerInstance = crawler.Crawler(domain)
        while not self.jobQueue.empty():
            currentURL = self.jobQueue.get()
            foundURLs = crawlerInstance.scrape(currentURL)
            for link in set(foundURLs):
                if re.match(domain, link) and link not in self.visitedURLs.keys():
                    self.jobQueue.put(link)
            self.visitedURLs[currentURL] = foundURLs
        return self.visitedURLs
                