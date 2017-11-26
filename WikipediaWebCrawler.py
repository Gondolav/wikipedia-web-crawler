import time
import urllib
import requests
from bs4 import BeautifulSoup

MAXIMUM_SEARCH_LENGTH = 25

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"
article_chain = [start_url]

def web_crawl():
    print("Searching...")
    while continue_crawl(article_chain, target_url):
        print(article_chain[-1])
        first_link = find_first_link(article_chain[-1])

        if not first_link:
            print("Current article has no links; search aborted")
            break

        article_chain.append(first_link)
        time.sleep(2)

def continue_crawl(search_history, target_url):
    if (search_history[-1] == target_url):
        print("Target article found; search completed")
        return False

    if (len(search_history) >= MAXIMUM_SEARCH_LENGTH):
        print("Search history has more than 25 entries; search aborted")
        return False

    if (len(search_history) > len(set(search_history))):
        print("Cycle detected; search aborted")
        return False;

    return True

def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    article_link = None

    for element in content_div.children:
        if element.p.a:
            first_relative_link = element.p.a.get('href')
            break

    if not article_link:
        return

    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link
