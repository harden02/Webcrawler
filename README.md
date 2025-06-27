# Webcrawler
A simple web crawler which goes through the in domain links on a given website, and prints out the links that are present. It also returns a dictionary of the links for easy analysis/retrieval. Made for the Monzo take-home test.
Output is in the form:
```bash
Base URL is : URL, found URLs: [URl1, URL2, ...]
```
Upon completion, it will return a dict of these URL to found URL relations and print out the URL keys that were visited:
```bash
Scraping completed. Visited URLs: dict_keys([URLs found])
```

## Usage
Make sure you have all of the packages installed from the requirements.txt, and python 3.12 or later.
Run from the app's base directory in your terminal.

arguments:
```bash
  inputURL                   The initial URL at which to start crawling. Format must be https://domain.com or domain.com
```
optional arguments:
```bash
  connectionfailure          What to do if the crawler is unable to retrieve a URL, continue to pass on to other URLs in the queue, stop to terminate with an error
  forcestandardURL           force standardization of URLs and their query parameters to avoid revisiting pages, y/n
```
Example run:
  ```bash
  python main.py google.com cont![Crawler drawio](https://github.com/user-attachments/assets/16a369e1-c45e-412c-a27b-f7fc591894df)
inue y
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
## Application design diagram
![Crawler drawio](https://github.com/user-attachments/assets/5477c27b-da38-4343-9b93-0e4cc8805b81)
