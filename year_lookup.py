from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


# html_page = urllib.request.urlopen("http://www.fifa.com/fifa-tournaments/archive/worldcup/index.html")
#
# soup = BeautifulSoup(html_page.read(), "html.parser")
#
# # soup = BeautifulSoup(html_page, "html.parser")

req = Request("https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals", headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

import pdb; pdb.set_trace()


# order_list = soup.find_all("li", {"class": "comp-item"})
#
# # import pdb, pdb.set_trace()
#
# print(order_list)
