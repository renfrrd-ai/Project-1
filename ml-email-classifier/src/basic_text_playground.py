from pathlib import Path
import re
import nltk
from nltk.corpus import stopwords


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


if __name__ == '__main__':
    email_text = read_email()
    cleaned_text = clean_text(email_text)
    print("RAW EMAIL:\n{}\n".format(email_text))
    print("CLEANED EMAIL:\n{}\n".format(cleaned_text))
    print("STATS:")
    text_stats(cleaned_text)
    tokens = tokenize(cleaned_text)  # tokenizing text
    tokens = remove_stopwords(tokens)  # removing stop words from tokens
    print(tokens[:20])
