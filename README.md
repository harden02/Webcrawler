# Webcrawler
A simple web crawler which goes through the in domain links on a given website, and prints out the links that are present. It also returns a dictionary of the links for easy analysis/retrieval. Made for the Monzo take-home test.

## Usage
arguments:
  inputURL                   The initial URL at which to start crawling. Format must be https://domain.com or domain.com

optional arguments:
  connectionfailure          What to do if the crawler is unable to retrieve a URL, continue to pass on to other URLs in the queue, stop to terminate with an error
  forcestandardURL           force standardization of URLs and their query parameters to avoid revisiting pages, y/n

Example run:
  ```bash
  python main.py https://astroviewer.net/ continue y
  ```
  This will run with a continue on connection failure and will force URL standardization
  

## Limitations

- Currently this will only crawl using the https protocol. Others could be added but extra security measures could be neccessary
- The application is currently only single threaded. This is to make sure that the scraping does not become rate-limited or redirected due to DDOS flagging. However, it is built to be extensible into a multi-threaded application with multiple controllers for scraping multiple domains, or multiple crawler instances to scrape the same domain.

## Testing
To run unit tests from the base directory:
  ```bash
  python -m unittest tests/testname.py
  ```
