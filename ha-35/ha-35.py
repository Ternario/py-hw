import requests
from bs4 import BeautifulSoup
from collections import Counter
import re


# ---------------- Task 1 ---------------------
def get_response(url: str):
    response = requests.get(url)
    code, status, headers = response.status_code, response.text, response.headers

    return code, status, headers


for i in get_response("https://www.google.com"):
    print(i)

# ---------------- Task 2 ---------------------
print("---------------- Task 2 ---------------------")


def find_common_words(url_list: list) -> list:
    all_textes = ""
    words_list = []

    for url in url_list:
        response = requests.get("https://" + url)
        soup = BeautifulSoup(response.text, "html.parser")
        founded_tags = soup.find_all("div")

        # Я не создавал доп переменных и запихнул все максимально компактно,
        # в таком формате это считается еще нормально или уже перебор и сложно читать?

        for text in [tag.get_text().strip().replace("\n", " ") for tag in founded_tags]:
            all_textes += text

    for key, value in Counter(re.findall(r"\b[a-zA-Zа-яА-ЯёЁ]+\b[2,]", all_textes)).most_common(10):
        words_list.append((key, value))

    return words_list


arr_url = ["ilibrary.ru/text/436/p.2/index.html", "ilibrary.ru/text/69/p.4/index.html"]
for i in find_common_words(arr_url):
    print(i)
