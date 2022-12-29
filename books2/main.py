from helpers.logger import setup_logger
from helpers.get_soup import getSoup
import pandas as pd

logger = setup_logger()
logger.info('logger is setup.')

data = []


def get_url(i): 
    return "https://books.toscrape.com/catalogue/page-{i}.html"
    
def main(): 
    for i in range(1, 5):
        logger.info(f"working on i = {i}")
        url = get_url(i)
        soup = getSoup(url)
        books = soup.find_all('article')

        for book in books:
            link = book.find('div', class_='image_container').find('a')['href'].strip()
            title = book.find('h3').find('a')['title']
            price = book.find('p', class_='price_color').text[1:].strip()
            availability = book.find('p', class_='instock availability').text.strip()
            result = {
                'title': title,
                'link': link,
                'price': price,
                'availability': availability
            }
            data.append(result)

    return data


data = main()
if data:
    logger.info("got to the df")
df = pd.DataFrame(data)
df.to_csv('books.csv', index=False)