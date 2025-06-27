import unittest
import sys
sys.path.append('..') #higher directory to import the application code
from app.startingURL import SeedURLSetup


class testStartingURL(unittest.TestCase):

    #unable to use standard setup due to the need for different URLs to be tested, will instantiate a SeedURLSetup object in each test
    
    #test a valid URL
    def testValidURL(self):
        urlSetup = SeedURLSetup("google.com")
        expected = "https://google.com"
        coercedURL = urlSetup.coerceURL()
        assert coercedURL == expected, f"Expected {expected}, got {coercedURL}"
        expectedDomain = "google.com"
        domain = urlSetup.getDomain(coercedURL)
        assert domain == expectedDomain, f"Expected {expectedDomain}, got {domain}"

    #test an invalid URL
    def testInvalidURL(self): 
        url = "apcdehg/silly"
        urlSetup = SeedURLSetup(url)
        self.assertRaises(ValueError, urlSetup.coerceURL)

    def testDomainError(self):
        url = "apcdehg/silly"
        urlSetup = SeedURLSetup(url)
        self.assertRaises(ValueError, urlSetup.getDomain, url)


if __name__ == '__main__':
    unittest.main()