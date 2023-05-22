from bs4 import BeautifulSoup
from requests import get

html = get("https://enter.kg/").text
soup = BeautifulSoup(html,"html.parser")
container = soup.find("ul",class_="VMmenu")
category_list=[x.text for x in container.find_all("a")]

def find_cotegory(catigories,keyword):
    return [x for x in catigories if keyword.lower() in x.lower()]

print(find_cotegory(category_list,"Ноутбуки"))