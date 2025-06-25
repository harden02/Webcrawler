from queue import Queue
import crawler
import re
import urllib.parse

class Controller:

    def __init__(self, domain, seedURL):
        self.domain = domain
        self.seedURL = seedURL
        self.jobQueue = Queue()
        self.visitedURLs = {self.seedURL}

    def startScraping(self):
        self.jobQueue.put(self.seedURL)
        crawlerInstance = crawler.Crawler(self.domain)
        while not self.jobQueue.empty():
            currentURL = self.jobQueue.get()
            foundURLs = crawlerInstance.scrape(currentURL)
            domainlink = "https://" + self.domain
            pattern = fr'^{domainlink}'
            print(f'pattern is {pattern}')
            for link in foundURLs:
                if re.match(pattern, link) and link not in self.visitedURLs:
                    self.jobQueue.put(link)
                    self.visitedURLs.add(link)
        return self.visitedURls
                