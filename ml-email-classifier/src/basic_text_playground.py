from pathlib import Path
import re


def read_email():
    email_path = Path(__file__).parent.parent / "data" / \
        "raw" / 'example_email.txt'
    with open(email_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text


def clean_text(raw_text: str) -> str:
    raw_text = raw_text.lower()
    URL_PATTERN = r'https?://\S+|www\.\S+'

    text = re.sub(URL_PATTERN, "", raw_text)
    text = re.sub(r'\s+', " ", text)
    text = re.sub("subject:", "", text)  # text is lowercase

    text = text.strip()

    return text


if __name__ == '__main__':
    email_text = read_email()
    print(clean_text(email_text))
