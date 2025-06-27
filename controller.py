from queue import Queue
from crawler import Crawler
import urllib.parse

class Controller:
    """
    Controller class to manage the web scraping process, including URL standardization, queue management, and interaction with the Crawler class.
    """

    def __init__(self, domain, seedURL, forceStandardURL, failoverAction):
        self.domain = domain #domain to scrape
        self.seedURL = seedURL #formatted initial url
        self.jobQueue = Queue() #queue of URLs to scrape
        self.visitedURLs = set() #URLs that have been visited before
        self.URLmap = {} #dict of URLs and the links found on the page
        self.forceStandardURL = forceStandardURL
        self.failoverAction = failoverAction

    def setupController(self):
        """
        Initializes a controller with a queue and visited URL set to feed to the crawler. Populates these with the seed URL.
        """
        standardizedURL = self.standardizeURL(self.seedURL)
        #add initial URL to queue and visited set
        self.jobQueue.put(standardizedURL)
        self.visitedURLs.add(standardizedURL)
        print(f'initialized queue with seed URL: {standardizedURL}')


    def startScraping(self, domain):
        """
        Starts the scraping process by creating and tasking the crawler to scrape the URLs.
        Manages the queue of URLs and sorts the crawler returned URLs into the visited set and queue if they aren't seen before and in domain.
        Continues until the queue is empty.
        """
        #ser up crawler instance
        crawlerInstance = Crawler(domain, self.failoverAction)
        print(f"domain to crawl is: {domain}")
        #whilst the queue is not empty, pass the top URL to the crawler and get the links found on that page
        while not self.jobQueue.empty():
            currentURL = self.jobQueue.get()
            foundURLs = crawlerInstance.scrape(currentURL)
            #iterate through the found URLs, standardize them, and add them to the queue/visited list if they haven't been visited and are in domain
            for link in set(foundURLs):
                standardizedLink = self.standardizeURL(link)
                if urllib.parse.urlparse(standardizedLink).netloc == domain and standardizedLink not in self.visitedURLs:
                    self.jobQueue.put(standardizedLink)
                    self.visitedURLs.add(standardizedLink)
            self.URLmap[currentURL] = foundURLs
        #return the URL dict for easy analysis of the links found
        return self.URLmap
    
    def standardizeURL(self, url):
        """
        Class to standardize the initial and incoming URLs to a consistent format by ordering the queries and removing trailing slashes.
        """
        try:
            #retrieve url parameters
            parsedURL = urllib.parse.urlparse(url)
            netloc = parsedURL.netloc
            path = parsedURL.path.rstrip('/')
            #sort the URL query
            query = urllib.parse.urlencode(sorted(urllib.parse.parse_qsl(parsedURL.query)))
            return urllib.parse.urlunparse((parsedURL.scheme, netloc, path, '', query, ''))
        except ValueError:
            print(f"unable to standardize URL")
            if self.forcestandardURL == 'y':
                print(f"Continuing with original seed URL format. This may lead to repeated URL visits or errors.")
                return url
            else:
                raise 