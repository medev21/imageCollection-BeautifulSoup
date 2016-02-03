from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


# html_page = urllib.request.urlopen("http://www.fifa.com/fifa-tournaments/archive/worldcup/index.html")
#
# soup = BeautifulSoup(html_page.read(), "html.parser")
#
# # soup = BeautifulSoup(html_page, "html.parser")

req = Request("http://www.fifa.com/fifa-tournaments/archive/worldcup/index.html", headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()


page_soup = BeautifulSoup(webpage, "html.parser")
order_list = page_soup.find_all("a", {"class": "link-wrap"})
#
#
# print(order_list)

# import pdb; pdb.set_trace()

print(type(order_list[0]))
