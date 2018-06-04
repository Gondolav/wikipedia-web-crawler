import crawler

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"
MAXIMUM_SEARCH_LENGTH = 25

crawler.web_crawl(start_url, target_url, 25)
