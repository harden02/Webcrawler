import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

class SeedURLSetup:
   
    def __init__(self, url):
        self.url = url

    def coerceURL(self):
        if not self.url.startswith('http'):
            try:
                abslink = "https://" + self.url
                return abslink
            except ValueError:
                print(f"Unable to coerce URL into valid format! Please try using the full link.")
                sys.exit(1)
        return self.url

    def getDomain(self, inputURL):
        domain = urllib.parse.urlparse(inputURL).netloc
        print(f"Domain is: {domain}")
        return domain
        