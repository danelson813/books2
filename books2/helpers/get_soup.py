import requests
from bs4 import BeautifulSoup as BS

def getSoup(url):
    res = requests.get(url)
    soup = BS(res.content, 'html.parser')
    return soup

if __name__ == '__main__':
    getSoup('https://books.toscrape.com')