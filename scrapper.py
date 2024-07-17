from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient
import time
import datetime
from datetime import timezone


client = MongoClient("mongodb+srv://username:password@cluster0.ccyzc4c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.GameDB


def insertToDb(page, title, link):
    collection = db[page]
    doc = {
        "title": title,
        "link": link,
        "date": datetime.datetime.now(timezone.utc)
    }
    inserted = collection.insert_one(doc)
    return inserted.inserted_id


driver = webdriver.Chrome()

page = "games"
for i in range(1,2):
    url = f'https://dodi-repacks.site/page/{i}/'

 
    driver.get(url)

 
    time.sleep(2) 


    main_section = driver.find_element(By.ID, 'main')

   
    titles = []
    torrent_links = []

  
    articles = main_section.find_elements(By.TAG_NAME, 'article')

  
    for article in articles:
        try:
         
            title_element = article.find_element(By.CLASS_NAME, 'entry-title')
            title = title_element.text.strip()
        except NoSuchElementException:
            title = "Title Not Found"

        try:
          
            torrent_link_element = article.find_element(By.CSS_SELECTOR, 'p a[href*="up-4ever.net"], p a[href*="upload-4ever.com"], p a[href*="file-upload.com"]')
            torrent_link = torrent_link_element.get_attribute('href')
        except NoSuchElementException:
            torrent_link = "Torrent Link Not Found"

   
        titles.append(title)
        torrent_links.append(torrent_link)

      
        insertToDb(page, title, torrent_link)

   
    for title, link in zip(titles, torrent_links):
        print(f"Title: {title}")
        print(f"Torrent Link: {link}")
        print()


driver.quit()
