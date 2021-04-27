import argparse
import random
import csv
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from time import sleep

#!/usr/bin/env python3

PATH = "C:\Program Files (x86)\chromedriver.exe"
user_agent = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
#test = "https://mobile.facebook.com/15408433177/posts/10158413687398178"
#test2 = "https://mobile.facebook.com/story.php?story_fbid=10158433126738178&id=15408433177"

def setup(options):
    #options = Options()
    # if headless option is giving you errors that make the program break, disable it
    #options.add_argument("--headless")
    # sandbox needed to allow headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--incognito')
    options.add_argument(user_agent)

def login(driver):
    with open("credentials.txt") as file:
        email = file.readline().split()[2]
        password = file.readline().split()[2]

    driver.get("https://mobile.facebook.com/")
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_name("login").click()
    driver.implicitly_wait(3)

def scroll(driver):
    scroll_time = 0.5
    width = 400

    # xpath for the load comments button
    sub1 = "/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[2]/div/div/div[4]/div[1]/a"
    sub2 = "/div[1]"
    sub3 = "/html/body/div[1]/div/div[3]/div[3]/div/div/div[2]/div/div[3]/div[1]/a"

    driver.implicitly_wait(3)
    driver.execute_script("window.scrollTo(0, 1000);")

    while True:
        try:
            sum = driver.find_element_by_xpath(sub3)
        except:
            break

        sleep(0.3)
        sum.click()
        sub3 = sub3[:-2] + sub2 + sub3[-2:]
    
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 2000")


def is_question(comment):
    # move searching for ? or not
    questions = ["who", "what", "how", "when", "where"]
    for v_word in questions:
        if re.search(rf"\b{v_word}.*\b", comment):
            return True 
    return False

def get_comments(driver):
    soup = bs(driver.page_source, "html.parser")

    post_box = soup.find(id="m_story_permalink_view")
    posts = post_box.find_all("div", attrs={"data-sigil": "comment-body"})

    comments = []
    #num = 0

    for post in posts:
        obj = re.compile(r"\w+\?\s*")
        comment = post.get_text().strip()

        if obj.search(comment):
            comments.append(comment)
        elif is_question(comment):
            comments.append(comment)
    
    #print("how many comments?")
    #print(num)
    #print(len(comments))

    with open("facebook_data.csv", "w+", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["Questions/Comments"])

        for x in comments:
            writer.writerow([x])

# m_story_permalink_view
# _2a_m for replies?
# data-sigil = "comment-body"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Facebook Data Scraping program. Web scrapes questions from a post's comments.")
    #parser.add_argument("-url", "-u", help="Facebook public post you want to scrape", required=True)
    parser.add_argument('link', metavar='url', help="Facebook public post you want to scrape for questions.")

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
