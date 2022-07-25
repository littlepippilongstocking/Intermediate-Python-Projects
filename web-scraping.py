"""
Dilyana Koleva, July 2022
Intermediate Python Projects - Web Scraping Program
22.07.22 - Only for profile picture
25.07.22 - Added option to scrape a job board for python jobs or for all jobs
"""
import requests
from bs4 import BeautifulSoup as bs


def decide():
    txt = input("Welcome to Web Scraper. Do you want to scrape github (github) or python jobs (jobs)? ").lower()
    if txt == "github":
        git()
    elif txt == "jobs":
        jobs()


def git():
    github_user = input("Github Username:")
    url_git = "https://github.com/" + github_user
    req_git = requests.get(url_git)
    soup = bs(req_git.content, "html.parser")

    profile_image = soup.find("img", {"alt": "Avatar"})["src"]
    print(profile_image)


def jobs():
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)
    # print(page.text) #fetches the static site content from the Internet
    soup = bs(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    # print(results.prettify())

    job_elements = results.find_all("div", class_="card-content")
    for job_element in job_elements:  # prints out all jobs
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        # print(title_element.text.strip())
        # print(company_element.text.strip())
        # print(location_element.text.strip())
        # print()

    python_jobs = results.find_all(
        "h2", string=lambda text: "python" in text.lower()
    )

    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

    for job_element in python_job_elements:  # prints out only python related jobs
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print()
        links = job_element.find_all("a")
        link_url = job_element.find_all("a")[1]["href"]
        print(f"Apply here: {link_url}\n")


decide()
