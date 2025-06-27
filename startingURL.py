import urllib.parse
import re

class SeedURLSetup:
   
    def __init__(self, url):
        self.url = url

    def coerceURL(self):
        """ 
        Coerce the URL into a standard format, ensuring it starts with 'http://' or 'https:// and running a regex check.
        If the URL is malformed, raise an error.
        """
        if not self.url.startswith('http'):
                abslink = "https://" + self.url
        else:
            abslink = self.url
        pattern = re.compile(r'^(https?://)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})')
        if pattern.match(abslink):
             print(f"Coerced URL is: {abslink}")
             return abslink
        else:
            raise ValueError(f"Unable to coerce URL into valid format! Please provide the URL as either a full link or a domain name. URL provided: {self.url}")

    def getDomain(self, inputURL):
        """
        Extract the domain from the input URL.
        """
        domain = urllib.parse.urlparse(inputURL).netloc
        if domain:
            print(f"Domain is: {domain}")
            return domain
        else:
            raise ValueError(f"Unable to extract domain from URL: {inputURL}")
 
        