import re
from lxml import html
import sys
import bs4
import requests
from pathlib import Path

DOWNLOAD_DIR =  str(Path.home()) + '/Downloads/Anime/'

def getURL():
    if len(sys.argv) < 2:
        return input("Enter URL::\t")
    else:
        return sys.argv[1]


def generation(link, episodes):
    session = Generator(link, episodes)
    res = session.generate()

    if res == -1:
        print("We don't support this format, please check documentation")
    else:
        with open(DOWNLOAD_DIR + 'q.txt', 'a') as f:
            for i in res:
                f.write(i+'\n')
        f.close()


def epList(i):
    if len(sys.argv) < 3:
        res = list(map(int, input(
            "Enter episode range (space separated)::\t").split()))
        if res != '' or res != None:
            if res[0] <= i:
                return res
            else:
                print("Try Again within limits.")
                epList(i)
        else:
            return [x for x in range(1, i+1)]
    elif len(sys.argv) == 4:
        return [x for x in range(int(sys.argv[2]), int(sys.argv[3])+1)]
    else:
        return sys.argv[2:]


class Generator:
    def __init__(self, link, episodes):
        self.link = link
        self.episodes = episodes

    def loop(self):
        for episode in self.episodes:
            yield (self.giveBack(episode))

    def giveBack(self, number):
        size = len(re.search("-0{0,2}1-1080p", self.link).group()) - 7
        number = str(number).zfill(size)
        return (re.sub("-0{0,2}1-1080p", "-%s-1080p" % number, self.link))

    def generate(self):
        if(self.link.find('?') + 1):
            self.link = self.link[:self.link.index('?')].replace(
                '://', '://storage.googleapis.com/justawesome-183319.appspot.com/')
        if(re.search("-0{0,2}1-1080p", self.link)):
            return list(self.loop())
        else:
            return -1


def getLink(URL, i=1):
    page = requests.get(URL)
    soup_main = bs4.BeautifulSoup(page.text, 'html.parser')
    title = soup_main.find('p', {'class': 'single-anime-desktop'}).text
    chap = soup_main.find('ul', {'class': 'episodes range active'})
    eplinks = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                         str(chap))
    eps = requests.get(eplinks[0])
    epsl = bs4.BeautifulSoup(eps.content, 'lxml')
    link = epsl.find(
        type='video/mp4')['src'].replace('mountainoservoo002', 'mountainoservo0002')
    return title, link, len(eplinks)
