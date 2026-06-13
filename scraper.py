from bs4 import BeautifulSoup
import requests
import pandas as pd

try:
    rows = []
    for i in range(1, 51):
        response = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
        response.encoding = response.apparent_encoding or 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        books_list = soup.find('ol', class_='row')
        if not books_list:
            continue
        books = books_list.find_all('li')
        for book in books:
            book_name = book.find('article', class_='product_pod')
            book_price = book.find('p', class_='price_color')
            rating = book_name.find('p', class_='star-rating')
            stock = book.find('p', class_='instock availability')
            if not book_name:
                continue

            name = book_name.find('h3').find('a').get('title', '').strip()
            price = book_price.get_text(strip=True).replace('£', '') if book_price else ''
            in_stock = stock.get_text(strip=True) if stock else ''
            rating_value = rating.get('class')[-1] if rating else ''

            rows.append({'Book Name': name, 'Price (£)': price, 'In Stock': in_stock, 'Rating': rating_value})

    df = pd.DataFrame(rows, columns=['Book Name', 'Price (£)', 'In Stock', 'Rating'])
    df.to_csv('data//books.csv', index=False,header=['Book Name', 'Price (£)', 'Stock Availability', 'Rating'])
except Exception as e:
    print(f"An error occurred: {e}")
