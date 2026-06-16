from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def scrape(link):
    response1 = requests.get(link, headers=headers)
    response1.encoding = response1.apparent_encoding or 'utf-8'
    soup = BeautifulSoup(response1.text, 'html.parser')
    book = soup.find('div', class_='col-sm-6 product_main')
    book_name = soup.find('h1')
    book_price = soup.find('p', class_='price_color')
    rating = book.find('p', class_='star-rating')
    quantity = book.find('p', class_='instock availability')

    book_name = book_name.get_text(strip=True) if book_name else ''
    book_price = book_price.get_text(strip=True).replace('£', '') if book_price else ''
    rating = rating.get('class')[-1] if rating and rating.get('class') else ''
    quantity_text = quantity.get_text(strip=True) if quantity else ''
    return book_name, book_price, rating, quantity_text[10:12]

try:
    rows = []
    for i in range(1, 51): 
        response = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html", headers=headers)
        response.encoding = response.apparent_encoding or 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        books_list = soup.find('ol', class_='row')
        if not books_list:
            continue
        books = books_list.find_all('li')
        for book in books:
            link = book.find('a')
            if not link:
                continue
            href = link.get('href', '').strip()
            product_link = urljoin(response.url, href)
            rows.append(scrape(product_link))
    df = pd.DataFrame(rows, columns=['Book Name', 'Price (£)', 'Rating', 'Quantity'])
    df.to_csv('data//books.csv', index=False,header=['Book Name', 'Price (£)', 'Rating', 'Quantity'])
except Exception as e:
    print(f"An error occurred: {e}")
