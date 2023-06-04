import requests
import json
import urllib.request
from bs4 import BeautifulSoup, Tag
from selenium import webdriver
import functools
import re

def scrapePage(url):
    chapterContent = ""
    # If so first get 'chapter-inner chapter-content' class
    # Then combine all 'p' tags into one block of text
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Use regit to check if RR site
    if "royalroad.com" in url:
        chapterHTML = soup.find('div', {"class": "chapter-inner chapter-content"})
        chapterRaw = map(lambda a: a.text, chapterHTML.find_all('p'))
        chapterContent = functools.reduce(lambda a, b: a + b, chapterRaw)
    else:
        chapterRaw = map(lambda a: a.text, soup.find_all('p'))
        chapterContent = functools.reduce(lambda a, b: a + b, chapterRaw)
    print(chapterContent)
    return chapterContent