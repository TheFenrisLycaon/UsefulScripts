from re import sub, compile
from string import punctuation
from time import process_time
import pandas as pd
from nltk.corpus import stopwords, gutenberg
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from unidecode import unidecode

emma = gutenberg.words("austen-emma.txt")
example_text = " ".join(emma)
df = pd.DataFrame(data={"sentences": sent_tokenize(example_text)})


def tokenizer(s):
    return clean_text(s).split()


vectorizer = CountVectorizer(
    encoding="ascii",
    decode_error="ignore",
    strip_accents="ascii",
    tokenizer=tokenizer,
    lowercase=False,
    max_df=0.7,
    min_df=0.0001,
)

vectorizer.fit(df["sentences"])
STOP_WORDS = stopwords.words("english")
pattern_cleaning = compile(r"[^\w\s]|\d")
pattern_stop_words = compile(r"\b(" + r"|".join(STOP_WORDS) + r")\b\s*")


def remove_punctuation_r(s):
    return sub(pattern_stop_words, "", sub(pattern_cleaning, "", s.lower()))


def remove_short_words(s):
    return " ".join([w for w in s.split() if len(w) > 2])


def clean_text(s):
    return remove_short_words(remove_punctuation_r(s))


pattern_cleaning = compile(r"[^\w\s]|\d")
pattern_stop_words = compile(r"\b(" + r"|".join(stopwords.words("english")) + r")\b\s*")
pattern_short_words = compile(r"\b[^\s]{0,2}\b")
exclude = punctuation


def remove_punctuation_t(s):
    return unidecode(s).translate(str.maketrans("", "", exclude)).lower()


def remove_punctuation_r(s):
    return sub(pattern_stop_words, "", sub(pattern_cleaning, "", s.lower()))


def remove_stop_words(s):
    return " ".join([word for word in s.split() if word not in STOP_WORDS])


def remove_stop_words_2(s):
    return sub(pattern_stop_words, "", s)


def remove_stop_words_3(s):
    return " ".join([w for w in s.split() if len(w) > 2 and not w in STOP_WORDS])


def remove_short_words(s):
    return " ".join([w for w in s.split() if len(w) > 2])


def remove_short_words_2(s):
    return sub(pattern_stop_words, "", s)


def clean_text_1(s):
    return remove_short_words_2(remove_punctuation_r(s))


def clean_text_2(s):
    return remove_short_words(remove_punctuation_r(s))


def clean_text_3(s):
    return remove_stop_words(remove_short_words(remove_punctuation_t(s)))


def clean_text_4(s):
    return remove_stop_words_3(remove_punctuation_t(s))


def clean_text_5(s):
    return remove_stop_words_3(remove_punctuation_r(s))


func = (clean_text_1, clean_text_2, clean_text_3, clean_text_4, clean_text_5)

title = (
    "Regex and unidecode, loop (short words)",
    "Regex and unidecode, filter (short words)",
    "Translate and unidecode, filter (short words) ,loops (stop words)",
    "Translate and unidecode, filter (short words, stop words)",
    "Regex, loop (short words, stop words)",
)

for f, t in zip(func, title):
    print(("*" * len(t)))
    print(t)
    print(("*" * len(t)))
    t0 = process_time()
    print((df["sentences"].apply(f).head()))
    print(f"Time: {process_time() - t0}")