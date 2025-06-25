import crawler
import requests
import startingURL
import controller

def main(inputURL):
    seedURL = startingURL.SeedURLSetup(inputURL)
    coercedURL = seedURL.coerceURL()
    domain = seedURL.getDomain(coercedURL)
    
    controllerInstance = controller.Controller(domain, coercedURL)
    controllerInstance.setupController()
    controllerInstance.startScraping(domain)
    print(f"Scraping completed. Visited URLs: {controllerInstance.URLmap.keys()}")

if __name__ == '__main__':
    inputURL = input("Please enter the URL to start scraping from: ")
    main(inputURL)