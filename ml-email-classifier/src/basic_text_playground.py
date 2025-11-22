from pathlib import Path
import re
import nltk
from nltk.corpus import stopwords


def read_email(file_path: Path) -> str:
    """Reads an email file and returns its contents as a string."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def clean_text(raw_text: str) -> str:
    raw_text = raw_text.lower()
    URL_PATTERN = r'https?://\S+|www\.\S+'

    text = re.sub(URL_PATTERN, "", raw_text)
    text = re.sub(r'\s+', " ", text)
    text = re.sub("subject:", "", text)  # text is lowercase

    text = text.strip()

    return text


def text_stats(text: str) -> None:
    print("No of chars: ", len(text))
    words = text.split()
    unique_words = list(set(words))
    print("No of words: ", len(words))
    print("No of unique words: ", len(unique_words))
    print("Five sample words: ", unique_words[:5])


def tokenize(text: str) -> list[str]:
    tokenized_words = nltk.word_tokenize(text)
    return tokenized_words


def remove_stopwords(tokens: list[str]) -> list[str]:
    return [token for token in tokens if token not in stopwords.words('english')]


def load_dataset() -> tuple[list[str], list[str]]:
    """Loads all emails, cleans them, and returns (texts, labels)."""

    emails_dir = Path(__file__).parent.parent / "data" / "raw" / "emails"

    texts = []
    labels = []

    for file_path in emails_dir.iterdir():
        if file_path.suffix != ".txt":
            continue

        raw_text = read_email(file_path)
        cleaned = clean_text(raw_text)
        texts.append(cleaned)

        if "spam" in file_path.name.lower():
            labels.append("spam")
        else:
            labels.append("ham")

    return texts, labels


if __name__ == '__main__':
    texts, labels = load_dataset()
    print(f"Loaded {len(texts)} emails")
    print(f"Spam: {labels.count('spam')}")
    print(f"Ham: {labels.count('ham')}\n")
    print("Example spam:\n", texts[labels.index('spam')][:200], "\n")
    print("Example ham:\n", texts[labels.index('ham')][:200], "\n")
