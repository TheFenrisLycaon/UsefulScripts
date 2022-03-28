# This script helps us to enter a word and get precise meaning for that word from vocabulary.com

import urllib.request
from bs4 import BeautifulSoup


def clean(text):

    TEXT = (
        text.replace("\xe2\x80\x99", "'")
        .replace("\xc3\xa9", "e")
        .replace("\xe2\x80\x90", "-")
        .replace("\xe2\x80\x91", "-")
        .replace("\xe2\x80\x92", "-")
        .replace("\xe2\x80\x93", "-")
        .replace("\xe2\x80\x94", "-")
        .replace("\xe2\x80\x94", "-")
        .replace("\xe2\x80\x98", "'")
        .replace("\xe2\x80\x9b", "'")
        .replace("\xe2\x80\x9c", '"')
        .replace("\xe2\x80\x9c", '"')
        .replace("\xe2\x80\x9d", '"')
        .replace("\xe2\x80\x9e", '"')
        .replace("\xe2\x80\x9f", '"')
        .replace("\xe2\x80\xa6", "...")
        .replace("\xe2\x80\xb2", "'")
        .replace("\xe2\x80\xb3", "'")
        .replace("\xe2\x80\xb4", "'")
        .replace("\xe2\x80\xb5", "'")
        .replace("\xe2\x80\xb6", "'")
        .replace("\xe2\x80\xb7", "'")
        .replace("\xe2\x81\xba", "+")
        .replace("\xe2\x81\xbb", "-")
        .replace("\xe2\x81\xbc", "=")
        .replace("\xe2\x81\xbd", "(")
        .replace("\xe2\x81\xbe", ")")
    )
    return TEXT.encode("utf-8")


word = eval(input("Enter the word of which you want to find the meaning: "))

# Get the meaning by scrapping www.vocabulary.com
url = "https://www.vocabulary.com/dictionary/" + word
htmlfile = urllib.request.urlopen(url)
soup = BeautifulSoup(htmlfile, "lxml")
soup1 = soup.find(class_="short")

try:
    soup1 = soup1.get_text()
except AttributeError:
    print("Cannot find such word! Check spelling.")
    exit()

# Print short meaning
print(("-" * 25 + "->", word, "<-" + "-" * 25))
print(("Short Meaning::\t", clean(soup1)))
print(("-" * 65))

# Print long meaning
soup2 = soup.find(class_="long")
soup2 = soup2.get_text()


if "y" in str(eval(input("Want more info ::(y/n)\t"))):
    print(("Long Meaning::\t", clean(soup2)))
print(("-" * 65))
# Print instances like Synonyms, Antonyms, etc.
soup3 = soup.find(class_="instances")
txt = soup3.get_text()
txt1 = txt.rstrip()

print((" ".join(txt1.split())))
