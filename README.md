
# 🎮 Dodi-Repack Scraper

This project is a web scraper that extracts game titles and torrent download links from the Dodi-Repack website and saves the data to a MongoDB database.

## 🌟 Features

- 🕸️ **Web Scraping**: Utilizes Selenium to navigate and scrape data from the Dodi-Repack website.
- 📝 **Data Extraction**: Extracts game titles and associated torrent download links from each page.
- 💾 **Database Storage**: Saves the scraped data to a MongoDB database with a timestamp.

## 🚀 Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/debasish26/DODI-Repack-Scraper.git
    cd DODI-Repack-Scrapper
    ```

2. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your MongoDB connection:**
   Update the MongoDB connection string in the script with your credentials:
    ```python
    client = MongoClient("your_mongodb_connection_string")
    ```

## 🛠️ Usage

1. **Run the scraper script:**
    ```bash
    python3 scrapper.py
    ```

2. **Scraped Data:**
   - The script will navigate through the specified pages of the Dodi-Repack website.
   - It extracts the game titles and torrent links and saves them to the MongoDB database in the specified collection.

3. **Check the console output:**
   - The script will print out the titles and torrent links it has scraped.

## 📚 Example

```python
Title: Game Title Example
Torrent Link: https://up-4ever.net/example
```

## 📦 Dependencies

- Python 3.x
- Selenium
- PyMongo
- ChromeDriver

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.
