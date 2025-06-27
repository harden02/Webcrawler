import urllib.parse

class SeedURLSetup:
   
    def __init__(self, url):
        self.url = url

    def coerceURL(self):
        """ 
        Coerce the URL into a standard format, ensuring it starts with 'http://' or 'https://
        if the URL is malformed, raise an error.
        """
        if not self.url.startswith('http'):
            try:
                abslink = "https://" + self.url
                return abslink
            except ValueError:
                print(f"Unable to coerce URL into valid format! Please try using the full link.")
                raise
        return self.url

    def getDomain(self, inputURL):
        """
        Extract the domain from the input URL.
        """
        try:
            domain = urllib.parse.urlparse(inputURL).netloc
            print(f"Domain is: {domain}")
            return domain
        except ValueError:
            print(f"unable to extract domain from URL: {inputURL}")
            raise 
        