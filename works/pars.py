from bs4 import BeautifulSoup
import requests
import csv

def get_html(url):
    response = requests.get(url)
    return response.text
 
def get_soup(html):
    soup=BeautifulSoup(html,"lxml")
    return soup

def get_1page_links(soup):
    ls=[]
    container=soup.find("div",class_="itemList")
    titles=container.find_all("a")
    ls.append(titles)
    return ls

html=get_html("https://vesti.kg/")
soup=get_soup(html)
print(get_1page_links(soup))