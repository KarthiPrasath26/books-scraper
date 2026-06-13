# 📚 Books to Scrape Web Scraper

A Python web scraping project that extracts book information from the **Books to Scrape** website and stores the collected data in a CSV file.

## 🚀 Features

* Scrapes data from all 50 catalogue pages.
* Extracts:

  * Book Title
  * Price (£)
  * Stock Availability
  * Rating
* Stores data in a structured CSV file.
* Uses error handling to prevent unexpected crashes.

---

## 🛠️ Technologies Used

* Python 3.x
* BeautifulSoup4
* Requests
* Pandas

---

## 📦 Required Libraries

Install the required dependencies:

```bash
pip install beautifulsoup4 requests pandas
```

---

## 📂 Project Structure

```text
project/
│
├── scraper.py
├── books.csv
└── README.md
```

---

## 📄 Dataset Fields

| Column Name        | Description                               |
| ------------------ | ----------------------------------------- |
| Book Name          | Title of the book                         |
| Price (£)          | Price of the book in British Pounds       |
| Stock Availability | Availability status of the book           |
| Rating             | Book rating (One, Two, Three, Four, Five) |

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/KarthiPrasath26/books-scraper.git
```

2. Navigate to the project directory:

```bash
cd books-scraper
```

3. Run the script:

```bash
python scraper.py
```

4. After execution, a file named `books.csv` will be generated in the project directory.

---

## 📊 Sample Output

| Book Name            | Price (£) | Stock Availability | Rating |
| -------------------- | --------- | ------------------ | ------ |
| A Light in the Attic | 51.77     | In stock           | Three  |
| Tipping the Velvet   | 53.74     | In stock           | One    |
| Soumission           | 50.10     | In stock           | One    |

---

## 🔍 Website Scraped

Target Website:

https://books.toscrape.com

This website is specifically designed for practicing web scraping and data extraction techniques.

---

## ⚙️ Working Principle

1. Send HTTP requests to catalogue pages.
2. Parse HTML content using BeautifulSoup.
3. Locate book information elements.
4. Extract title, price, rating, and stock status.
5. Store extracted records in a list.
6. Convert records into a Pandas DataFrame.
7. Export the DataFrame to a CSV file.

---

## ⚠️ Error Handling

The script includes a `try-except` block to handle unexpected exceptions during scraping and file generation.

```python
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## 📈 Future Improvements

* Export data to Excel format.
* Add book category extraction.
* Implement logging functionality.
* Add retry mechanism for failed requests.
* Store data in SQL databases.
* Create visualizations using Matplotlib or Power BI.

---

## 👨‍💻 Author

**Karthi Prasath**

Computer Science Student | Aspiring Data Analyst & Data Engineer

---

## 📜 License

This project is intended for educational and learning purposes.
