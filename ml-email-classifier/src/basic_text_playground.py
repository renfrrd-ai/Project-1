from pathlib import Path


def read_email():
    email_path = Path(__file__).parent.parent / "data" / \
        "raw" / 'example_email.txt'
    with open(email_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text


if __name__ == '__main__':
    email_text = read_email()
    print(email_text)
