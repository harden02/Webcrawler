import startingURL
import controller
import argparse



def parseArguments():
    parser = argparse.ArgumentParser("Web Crawler")
    parser.add_argument('inputURL', type=str, help='The URL to start scraping from')
    parser.add_argument('connectionfailure', type=str, help='Action to take on failure to connect to a URL, "continue" to ignore the url and continue crawling, or "stop" to terminate',
                         choices=['continue', 'stop'], default='stop', nargs='?')
    parser.add_argument('forcestandardURL', type=str, help='Force a standardized URL format, "y" to force, "n" to allow original format through if standardization fials',
                         choices=['y', 'n'], default='y', nargs='?')
    args = parser.parse_args()
    return args

def main():
    args = parseArguments()
    seedURL = startingURL.SeedURLSetup(args.inputURL)
    coercedURL = seedURL.coerceURL()
    domain = seedURL.getDomain(coercedURL)
    
    controllerInstance = controller.Controller(domain, coercedURL, args.forcestandardURL, args.connectionfailure)
    controllerInstance.setupController()
    controllerInstance.startScraping(domain)
    print(f"Scraping completed. Visited URLs: {controllerInstance.URLmap.keys()}")

if __name__ == '__main__':
    main()