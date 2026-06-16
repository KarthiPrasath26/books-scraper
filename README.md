# 📚 Books to Scrape — Web Scraper

A small Python scraper that extracts book information from the Books to Scrape demo site and saves results to CSV.

## 🚀 Features

* Scrapes data from catalogue pages (configurable page range).
* Extracts:

  * Book Title
  * Price (£)
  * Rating
  * Quantity
* Stores data in a structured CSV file (`data/books.csv`).
* Uses error handling to prevent unexpected crashes.

---

## 🛠️ Technologies Used

* Python 3.8+
* beautifulsoup4
* requests
* pandas

---

## 📦 Required Libraries

Install the required dependencies (recommended inside a virtualenv):

```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure

```text
e:/web scrape/
│
├── README.md
├── requirements.txt
├── scraper.py          # experimental: contains an alternative scraping flow
├── title_scrape.py     # main script (recommended)
└── data/
  └── books.csv       # output
```

---

## 📄 Dataset Fields

| Column Name        | Description                               |
| ------------------ | ----------------------------------------- |
| Book Name          | Title of the book                         |
| Price (£)          | Price of the book in British Pounds       |
| Rating             | Book rating (One, Two, Three, Four, Five) |
| Quantity           | Available stock (integer)                 |

---

## ▶️ How to Run

1. (Optional) Clone the repository or copy the project files to your local machine.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the main scraper:

```bash
python title_scrape.py
```

4. Output: `data/books.csv` will be created/updated with the scraped rows.

Note: `scraper.py` is an alternate/experimental script in the repo and may require fixes before use.

---

## 📊 Sample Output

| Book Name            | Price (£) | Rating | Quantity |
| -------------------- | --------- | ------ | -------- |
| A Light in the Attic | 51.77     | Three  | 22       |
| Tipping the Velvet   | 53.74     | One    | 20       |
| Soumission           | 50.10     | One    | 20       |

---

## 🔍 Website Scraped

Target website: https://books.toscrape.com

This website is specifically designed for practicing web scraping and data extraction techniques.

---

## ⚙️ Working Principle

1. Send HTTP requests to catalogue pages.
2. Parse HTML using BeautifulSoup.
3. Locate book information elements and extract fields.
4. Accumulate results into a Pandas DataFrame and export to CSV.

---

## ⚠️ Error Handling

The scripts include basic `try-except` error handling to avoid crashes. Consider adding retries and logging for production use.

---

## 📈 Future Improvements

* Export data to Excel format.
* Add book category and other metadata extraction.
* Implement robust logging and retry/backoff for requests.
* Store data in SQL databases or parquet files.
* Create visualizations using Matplotlib or Power BI.

---

## 👨‍💻 Author

**Karthi Prasath**

Computer Science Student | Aspiring Data Analyst & Data Engineer

---

## 📜 License

This project is intended for educational and learning purposes.
