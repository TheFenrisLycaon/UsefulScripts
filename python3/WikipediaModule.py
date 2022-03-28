
import wikipedia as wk
from bs4 import BeautifulSoup


def wiki():
    """
    Search Anything in wikipedia
    """

    word = eval(input("Wikipedia Search : "))
    results = wk.search(word)

    for i in enumerate(results):
        print(i)
    try:
        key = int(eval(input("Enter the number : ")))
    except AssertionError:
        key = int(eval(input("Please enter corresponding article number : ")))

    page = wk.page(results[key])
    url = page.url
    pageId = page.pageid
    title = page.title
    pageLength = eval(input("""Wiki Page Type : 1.Full 2.Summary : """))

    if pageLength == 1:
        soup = fullPage(page)
        print(soup)
    else:
        print(title)
        print("Page Id = ", pageId)
        print(page.summary)
        print("Page Link = ", url)
    pass


def fullPage(page):
    soup = BeautifulSoup(page.content, "lxml")
    return soup


def randomWiki():
    """
    This function gives you a list of n number of random articles
    Choose any article.
    """
    number = eval(input("No: of Random Pages : "))
    lst = wk.random(number)

    for i in enumerate(lst):
        print(i)
    try:
        key = eval(input("Enter the number : "))
        assert key >= 0 and key < number
    except AssertionError:
        key = eval(input("Please enter corresponding article number : "))

    page = wk.page(lst[key])
    url = page.url
    pageId = page.pageid
    title = page.title
    pageLength = eval(input("""Wiki Page Type : 1.Full 2.Summary : """))

    if pageLength == 1:
        soup = fullPage(page)
        print(soup)
    else:
        print(title)
        print("Page Id = ", pageId)
        print(page.summary)
        print("Page Link = ", url)
    pass


if __name__ == "__main__":
    wiki()
