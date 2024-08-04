import sys

print('Список параметров, переданных скрипту')
print(sys.argv)
print([arg for arg in sys.argv if arg[0] != '-'])


import re

# def highlight_keywords(text, keywords_arg):
#     tmp = '|'.join(map(re.escape, keywords_arg))
#     print(tmp)
#
#     new_text = re.sub(tmp, lambda x: f"*{x.group()}*", text, flags=re.IGNORECASE)
#
#     return new_text
#
#
# text_str = "This is a sample text. We need to highlight Python and programming."
# keywords = ["python", "programming"]
# print(highlight_keywords(text_str, keywords))


# ha 35

import requests
from collections import Counter
import re


# def get_response(url):
#     response = requests.get(url)
#
#     return response.headers
#
#
# print(get_response("https://lms.itcareerhub.de/mod/assign/view.php?id=3444"))

def find_common_words(url_list):
    for i in url_list:
        response = requests.get(i)
        text = re.findall(r'\b\w\b', response.text.lower())


find_common_words(['https://ilibrary.ru/text/436/p.2/index.html',
                   'https://ilibrary.ru/text/69/p.4/index.html'])
