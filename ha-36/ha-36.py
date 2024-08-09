import requests
from bs4 import BeautifulSoup


# ---------------- Task 1 ---------------------
def get_all_links(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a"):
        print(link["href"])


# get_all_links(input("Etner an URL-adress: "))


# ---------------- Task 2 ---------------------

def get_info_by_tag(url: str, tag: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all(tag):
        print(link)


get_info_by_tag(input("Enter an URL-adress: "), input("Enter tags name: "))
