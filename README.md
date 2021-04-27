# Social Media Question Finder
Scrapes Facebook and Twitter public posts comments for quesitons without using the Facebook or Twitter APIs.

# Install Requirements
Please make sure chrome is installed and PATH contains the correct path location to chromedriver file. By default,
the PATH variable leads to C: \ Programs File (x86).
Find out which version of chromedriver you need to download in this link: https://chromedriver.chromium.org/downloads

Please make sure you have installed python 3.
You can download all the additional modules using this command in the Linux terminal:
pip install -r requirements.txt

# Usage
## General
Scrapers are not allowed by most websites but are not illegal as long as you don't access private data.
Use sparingly to avoid being detected by the website or else you may be IP banned.
I would suggest using a VPN and logging out of your Facebook or Twitter account.

## Facebook:
Run this command on terminal: python facebook_scraper.py [link]
Note that this is run on facebook mobile for design purposes.
You can replace the www in the link with mobile to go to the mobile facebook website.
Example: python facebook_scraper.py https://mobile.facebook.com/15408433177/posts/10158413687398178

## Twitter:
Run this command on terminal: python twitter_scraper.py [link]
Example: python twitter_scraper.py https://twitter.com/DeptVetAffairs/status/1380286851974565892

# Note:
This program is meant to data scrape publicly available information and should in no way be used to obtain private information.
Please use this code for educational purposes only.
