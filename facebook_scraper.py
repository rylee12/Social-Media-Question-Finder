import random
import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from time import sleep, time

#if __name__ == "__main__":
#!/usr/bin/env python3

# //*[@id="see_prev_10158433126738178"]/a
# /html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[2]/div/div/div[4]/div[1]/a
#
# //*[@id="see_prev_10158430110018178"]/a
# /html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[2]/div/div/div[4]/div[1]/a
#
# //*[@id="see_prev_10158433126738178"]/a
# /html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a
# /html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[2]/div/div/div[4]/div[1]/div[1]/a

PATH = "C:\Program Files (x86)\chromedriver.exe"
#test = "https://www.facebook.com/15408433177/posts/10158413687398178"
test = "https://mobile.facebook.com/15408433177/posts/10158413687398178"
test2 = "https://mobile.facebook.com/story.php?story_fbid=10158433126738178&id=15408433177"

def setup(options):
    #options = Options()
    # if headless option is giving you errors that make the program break, disable it
    #options.add_argument("--headless")
    # sandbox needed to allow headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--incognito')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36")
    #dealer = webdriver.Chrome(options=options, executable_path=PATH)

def login(driver):
    with open("credentials.txt") as file:
        email = file.readline().split()[2]
        password = file.readline().split()[2]

    driver.get("https://mobile.facebook.com/")
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_name("login").click()
    driver.implicitly_wait(3)
    #//*[@id="root"]/div[1]/div/div/div[3]/div[1]/div/div/a
    #driver.find_element_by_xpath("//*[@id='root']/div[1]/div/div/div[3]/div[1]/div/div/a").click()
    #driver.implicitly_wait(2)

def question():
    print("questions")

def scroll(driver):
    print("scroll")
    scroll_time = 0.5
    width = 400

    sub1 = "/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[2]/div/div/div[4]/div[1]/a"
    sub2 = "/div[1]"
    sub3 = "/html/body/div[1]/div/div[3]/div[3]/div/div/div[2]/div/div[3]/div[1]/a"

    driver.implicitly_wait(3)
    driver.execute_script("window.scrollTo(0, 1000);")

    print(sub1)
    while True:
        try:
            sum = driver.find_element_by_xpath(sub3)
        except:
            break

        sleep(0.3)
        sum.click()
        sub3 = sub3[:-2] + sub2 + sub3[-2:]
        #print(sub1)
    
    print("got away")
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 2000")

    """

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        sleep(scroll_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    """

def get_comments(driver):
    print("navigate")
    #driver.find_element_by_id("m_story_permalink_view")
    soup = bs(driver.page_source, "html.parser")

    post_box = soup.find(id="m_story_permalink_view")
    posts = post_box.find_all("div", attrs={"data-sigil": "comment-body"})

    comments = []
    num = 0

    for post in posts:
        #print(post.get_text())
        comments.append(post.get_text().strip())
        num += 1
    
    print("how many comments?")
    print(num)
    print(len(comments))

    with open("data.csv", "w+", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["Questions/Comments"])

        for x in comments:
            writer.writerow([x])

# m_story_permalink_view
# _2a_m for replies?
# data-sigil = "comment-body"
# https://mobile.facebook.com/VeteransAffairs/posts

if __name__ == "__main__":
    print("main")
    options = Options()
    setup(options)
    driver = webdriver.Chrome(options=options, executable_path=PATH)
    #login(driver)
    #driver.get("https://mobile.facebook.com/15408433177/posts/10158413687398178")
    driver.get(test2)
    scroll(driver)

    get_comments(driver)

    sleep(6)

    driver.quit()
    #driver.close()