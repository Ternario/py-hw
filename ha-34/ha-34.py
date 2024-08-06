# ---------------- Task 1 ---------------------

import re


def extract_emails(text: str) -> list:
    return re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)


em_text = "Contact us at info@example.com or support@example.com for assistance."
print(extract_emails(em_text))

# ---------------- Task 2 ---------------------

import re


def highlight_keywords(text: str, keywords_arg: list) -> str:
    tmp = '|'.join(map(re.escape, keywords_arg))

    return re.sub(tmp, lambda x: f"*{x.group()}*", text, flags=re.IGNORECASE)


text_str = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]
print(highlight_keywords(text_str, keywords))
