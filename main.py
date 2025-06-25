import crawler
import requests
import startingURL
import controller

def main(inputURL):
    seedURL = startingURL.SeedURLSetup(inputURL)
    coercedURL = seedURL.coerceURL()
    domain = seedURL.getDomain()
    
    controllerInstance = controller.Controller(domain, coercedURL)
    controllerInstance.startScraping()

if __name__ == '__main__':
    inputURL = input("Please enter the URL to start scraping from: ")
    main(inputURL)