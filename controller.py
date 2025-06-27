from queue import Queue
from crawler import Crawler
import urllib.parse

class Controller:

    def __init__(self, domain, seedURL, forceStandardURL, failoverAction):
        self.domain = domain
        self.seedURL = seedURL
        self.jobQueue = Queue()
        self.visitedURLs = set()
        self.URLmap = {}
        self.forceStandardURL = forceStandardURL
        self.failoverAction = failoverAction

    def setupController(self):
        """
        Initializes a controller with a queue and visited URL set to feed to the crawler. Populates these with the seed URL.
        """
        standardizedURL = self.standardizeURL(self.seedURL)
        self.jobQueue.put(standardizedURL)
        self.visitedURLs.add(standardizedURL)
        print(f'initialized queue with seed URL: {standardizedURL}')


    def startScraping(self, domain):
        """
        Starts the scraping process by creating and tasking the crawler to scrape the URLs.
        Manages the queue of URLs and sorts the crawler returned URLs into the visited set and queue if they aren't seen before and in domain.
        Continues until the queue is empty.
        """
        crawlerInstance = Crawler(domain, self.failoverAction)
        print(f"domain to crawl is: {domain}")
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
    
    def standardizeURL(self, url):
        try:
            parsedURL = urllib.parse.urlparse(url)
            netloc = parsedURL.netloc
            path = parsedURL.path.rstrip('/')
            query = urllib.parse.urlencode(sorted(urllib.parse.parse_qsl(parsedURL.query)))
            return urllib.parse.urlunparse((parsedURL.scheme, netloc, path, '', query, ''))
        except ValueError:
            print(f"unable to standardize URL")
            if self.forcestandardURL == 'y':
                print(f"Continuing with original seed URL format. This may lead to repeated URL visits or errors.")
                return url
            else:
                raise 