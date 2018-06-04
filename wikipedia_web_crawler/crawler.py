import time
import urllib
import requests
from bs4 import BeautifulSoup

def web_crawl(start_url, target_url, maximum_search_length):
    """Starts crawling the web from start_url until target_url or the maximum search length is reached."""
    article_chain = [start_url]
    print("Searching...")
    while continue_crawl(article_chain, target_url, maximum_search_length):
        print(article_chain[-1])
        first_link = find_first_link(article_chain[-1])

        if not first_link:
            print("Current article has no links; search aborted")
            break

        article_chain.append(first_link)
        time.sleep(2)

def continue_crawl(search_history, target_url, maximum_search_length):
    if (search_history[-1] == target_url):
        print("Target article found; search completed")
        return False

    if (len(search_history) >= maximum_search_length):
        print("Search history has more than {length} entries; search aborted".format(length=maximum_search_length))
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

    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link
