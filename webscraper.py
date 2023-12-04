import requests
from bs4 import BeautifulSoup


def print_link_href(links):
    if links is not None:
        for link in links:
            print(link.get("href"))

def get_links(content):
    soup = BeautifulSoup(content, "html.parser")
    links = soup.find_all("a")
    return links

def get_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content
        return html_content
    else: 
        f"Failed to fetch, got {str(response.status_code)}"
    


url = ""
print_link_href(get_links(get_content(url)))