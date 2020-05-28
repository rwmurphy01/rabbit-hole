import requests
from bs4 import BeautifulSoup
import sys

def checkWikiLink(link):
    invalidLinks = ["/File", "/Wikipedia", "/Category", "/Help", "/Special", "/Portal", "/Talk", "/Main_Page", "/Template"] #Special wikipedia url's that aren't actual articles
    for invalidEnd in invalidLinks:
        if link[5:5 + len(invalidEnd)] == invalidEnd:
            return False

    return True

def getWikiLinksFromPage(url):
    page = requests.get(url) #requests the page

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll('a') #gets all of the links on the page

    wikiLinks = []
    for aTag in results:
        link = aTag.get('href')
        if link != None and link[0:5] == "/wiki" and checkWikiLink(link): #if the link found on the page is a link to a wikipedia article
            wikiLinks.append(link)

    return wikiLinks


def getArticleNamesFromPage(searchArticle):
    searchArticle = searchArticle.replace(' ', '_')

    searchUrl = "https://en.wikipedia.org/wiki/" + searchArticle
    articleLinks = getWikiLinksFromPage(searchUrl)

    articleNames = []
    for link in articleLinks:
        name = link[6:]
        name = name.replace("_", " ")
        if not ("%" in name):
            articleNames.append(name)

    return articleNames

def printGreeting():
    print()
    print("Hi! Welcome to Rabbit Hole.")
    print("To get started please enter a Wikipedia article name")
    print("All other articles present in that wikipedia article will be displayed")
    print("Then just type the next article you want to visit")
    print("Your current thread will also be displayed")
    print("Don't get lost! ;)")
    print("(Type quit to exit)")
    print()

currentThread = []

printGreeting()

start = True
searchArticle = input("Enter starting wikipedia article name: ")
if searchArticle == "quit":
    sys.exit()

while True:
    if not start:
        print("CURRENT THREAD: ", end = "")
        for thread in currentThread:
            print("-> " + thread, end=" ")
        print()
    while not start:
        try:
            searchArticle = input("Enter a wikipedia article name from the list: ")
            if searchArticle == "quit":
                sys.exit()
            articleNames.index(searchArticle)
            break
        except ValueError:
            print("This article was not in the previous articles (or the article name may have been misspelled)")

    start = False
    currentThread.append(searchArticle)
    articleNames = getArticleNamesFromPage(searchArticle)
    articleNames = set(articleNames)
    articleNames = list(articleNames)

    for article in articleNames:
        print(article)
    print()
