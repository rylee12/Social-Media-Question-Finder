# Social Media Question Finder
Scrapes Facebook and Twitter public posts comments for quesitons without using the Facebook or Twitter APIs.

# Install Requirements
Please make sure chrome is installed and PATH contains the correct path location to chromedriver file. By default,
the PATH variable leads to C: \ Programs File (x86).
Find out which version of chromedriver you need to download in this link: https://chromedriver.chromium.org/downloads

The files require the user agent of your computer. You can find your user agent using this website: https://www.whatismybrowser.com/detect/what-is-my-user-agent

Replace the user_agent variable with a string of your user agent.

Please make sure you have installed python 3.
You can download all the additional modules using this command in the Linux terminal:
pip install -r requirements.txt

To download the files, you can copy and paste the code into other python files or fork this repository and then clone the subsequent forked repository.
Or you can click on the clone button and download the files in a zip file and then extract the relevant files from there.

# Usage
## General
Scrapers are not allowed by most websites but are not illegal as long as you don't access private data.
Use sparingly to avoid being detected by the website or else you may be IP banned.
I would suggest using a VPN and logging out of your Facebook or Twitter account.

## Facebook:
Run this command on terminal to use the facebook scraper: python facebook_scraper.py [link]
IMPORTANT: The program only uses the mobile facebook website for design purposes so the links must be from the mobile facebook website.
To convert a facebook link to the mobile link, you can replace www with mobile.
Example: python facebook_scraper.py https://mobile.facebook.com/15408433177/posts/10158413687398178

## Twitter:
Run this command on terminal to use the twitter scraper: python twitter_scraper.py [link]
Example: python twitter_scraper.py https://twitter.com/DeptVetAffairs/status/1380286851974565892

# Note:
This program is meant to data scrape publicly available information and should in no way be used to obtain private information.
Please use this code for educational purposes only.
