import requests
from bs4 import BeautifulSoup
from lxml import etree
import re

ROOT_URL = "http://www.tennisabstract.com/charting/"

def get_page_xpath_result(url, xpath_str):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")
    dom = etree.HTML(str(soup))
    return dom.xpath(xpath_str)

match_links = get_page_xpath_result(ROOT_URL, '//a/@href')
matches = []

for link in match_links:
    if (re.match(r'^\d{8}', link) != None) and ('Novak_Djokovic' in link):
        res = get_page_xpath_result(ROOT_URL+link, '//td//b')[0].text
        matches.append(res)

result = ''
for match in matches:
    result += match + '\n'

f = open("matches.txt", "a")
f.write(result)
f.close()