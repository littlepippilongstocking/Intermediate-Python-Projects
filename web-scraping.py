"""
Dilyana Koleva, July 2022
Intermediate Python Projects - Web Scraping Program
22.07.22 - Only for profile picture
"""
import requests
from bs4 import BeautifulSoup as bs

github_user = input("Github Username:" )
url = "https://github.com/" + github_user
req = requests.get(url)
soup = bs(req.content, "html.parser")

profile_image = soup.find("img", {"alt" : "Avatar"})["src"]
print(profile_image)
