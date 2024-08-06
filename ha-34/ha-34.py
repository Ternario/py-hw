# ---------------- Task 1 ---------------------

import re


def extract_emails(text: str) -> list:
    return re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)


text = "Contact us at info@example.com or support@example.com for assistance."
print(extract_emails(text))

# ---------------- Task 2 ---------------------

import re


def highlight_keywords(text, keywords_arg):
    tmp = '|'.join(map(re.escape, keywords_arg))

    new_text = re.sub(tmp, lambda x: f"*{x.group()}*", text, flags=re.IGNORECASE)

    return new_text


text_str = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]
print(highlight_keywords(text_str, keywords))
