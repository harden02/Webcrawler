import unittest
from unittest.mock import patch
import sys
sys.path.append('..') #higher directory to import the application code
from controller import Controller


class testController(unittest.TestCase):

    #set up the controller
    def setUp(self):
        self.domain = "test.com"
        self.seedURL = "https://test.com"
        self.forceStandardURL = 'y'
        self.failoverAction = 'continue'
        self.controller = Controller(self.domain, self.seedURL, self.forceStandardURL, self.failoverAction)

    def testSetupController(self):
        #test the setup of the job queue and visited URL set
        self.controller.setupController()
        self.assertEqual(self.controller.jobQueue.qsize(), 1)
        self.assertIn(self.seedURL, self.controller.visitedURLs)
        self.assertEqual(self.controller.jobQueue.get(), self.seedURL)
    
    @patch('controller.Crawler')
    def testStartScraping(self, MockCrawler):
        #mock the Crawler class and its scrape method
        mockCrawlerInstance = MockCrawler.return_value
        mockCrawlerInstance.scrape.return_value = ["https://test.com/page1", "https://test.com/page2", "https://notdomain.com/page1"]
        
        #start scraping after setting up controller
        self.controller = Controller(self.domain, self.seedURL, self.forceStandardURL, self.failoverAction)
        self.controller.setupController()
        self.controller.startScraping(self.domain)
        
        #check that the URLs were visited
        self.assertIn("https://test.com/page1", self.controller.visitedURLs)
        self.assertIn("https://test.com/page2", self.controller.visitedURLs)
        self.assertNotIn("https://notdomain.com/page1", self.controller.visitedURLs)

    def testStandardizeURL(self):
        #test query sorting for URL
        url = "https://google.com/resource?query=2&1sort=asc"
        standardizedURL = self.controller.standardizeURL(url)
        expectedURL = "https://google.com/resource?1sort=asc&query=2"
        self.assertEqual(standardizedURL, expectedURL)



if __name__ == '__main__':
    unittest.main()