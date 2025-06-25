import crawler
import requests
import startingURL
import controller

def main(inputURL):
    seedURL = startingURL.SeedURLSetup(inputURL)
    coercedURL = seedURL.coerceURL()
    domain = seedURL.getDomain(coercedURL)
    
    controllerInstance = controller.Controller(domain, coercedURL)
    domainlink = controllerInstance.setupController()
    controllerInstance.startScraping(domainlink)
    print(f"Scraping completed. Visited URLs: {controllerInstance.visitedURLs.keys()}")

if __name__ == '__main__':
    inputURL = input("Please enter the URL to start scraping from: ")
    main(inputURL)