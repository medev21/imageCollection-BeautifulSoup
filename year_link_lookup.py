from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

# add user agent
req = Request("http://www.fifa.com/fifa-tournaments/archive/worldcup/index.html", headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()   #read the page


page_soup = BeautifulSoup(webpage, "html.parser") #parse the site
order_list = page_soup.find_all("a", {"class": "link-wrap"}, href=True) #extract anchor tags with class link-wrap and href is true

for item in order_list:
    print(item['href'])

import pdb; pdb.set_trace()

# print(type(order_list[0]))
