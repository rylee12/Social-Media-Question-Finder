import argparse
import random
import csv
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from time import sleep, time

PATH = "C:\Program Files (x86)\chromedriver.exe"
user_agent = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
scroll_pause = 1.5

#test = "https://twitter.com/DeptVetAffairs/status/1380286851974565892"
#test2 = "https://twitter.com/BarackObama/status/1384626851511951360"

def setup(options):
    #options = Options()
    # if headless option is giving you errors that make the program break, disable it
    #options.add_argument("--headless")
    # sandbox needed to allow headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--incognito')
    # add options for user agent
    options.add_argument(user_agent)

def is_question(comment):
    questions = ["who", "what", "how", "when", "where"]
    for v_word in questions:
        if re.search(rf"\b{v_word}.*\b", comment):
            return True
    return False

# twitter is infinite scroll, no clicking needed
# scroll to bottom of screen, wait for replies to load, repeat
def scroll(driver):
    last_height = 0
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # Load page
        sleep(scroll_pause)

        # Calculate new scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        # Compare with last height, break loop if not equal
        if new_height == last_height:
            break
        last_height = new_height

def get_comments(driver):
    soup = bs(driver.page_source, "html.parser")
    post_box = soup.find(attrs={"data-testid": "primaryColumn"})
    posts = post_box.find_all("span")

    comments = []

    for post in posts:
        obj = re.compile(r"\w+\?\s*")
        comment = post.get_text().strip()

        if obj.search(comment):
            comments.append(comment)
        elif is_question(comment):
            comments.append(comment)
    
    #print(comments)
    
    with open("twitter_data.csv", "w+", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["Questions/Comments"])

        for x in comments:
            writer.writerow([x])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Scraping Twitter program")
    parser.add_argument('link', metavar='url', help="Facebook public post you want to scrape")

    args = parser.parse_args()
    
    options = Options()
    setup(options)

    driver = webdriver.Chrome(options=options, executable_path=PATH)
    driver.get(args.link)
    sleep(2)

    scroll(driver)
    get_comments(driver)

    sleep(2)

    driver.quit()
