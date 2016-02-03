from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import re

url_list = [
            "/worldcup/archive/brazil2014/index.html",
            "/worldcup/archive/southafrica2010/index.html",
            "/worldcup/archive/germany2006/index.html",
            "/worldcup/archive/koreajapan2002/index.html",
            "/worldcup/archive/france1998/index.html",
            "/worldcup/archive/usa1994/index.html",
            "/worldcup/archive/italy1990/index.html",
            "/worldcup/archive/mexico1986/index.html",
            "/worldcup/archive/spain1982/index.html",
            "/worldcup/archive/argentina1978/index.html",
            "/worldcup/archive/germany1974/index.html",
            "/worldcup/archive/mexico1970/index.html",
            "/worldcup/archive/england1966/index.html",
            "/worldcup/archive/chile1962/index.html",
            "/worldcup/archive/sweden1958/index.html",
            "/worldcup/archive/switzerland1954/index.html",
            "/worldcup/archive/brazil1950/index.html",
            "/worldcup/archive/france1938/index.html",
            "/worldcup/archive/italy1934/index.html",
            "/worldcup/archive/uruguay1930/index.html"
]

for item in url_list:
    time.sleep(3) #sleep for 3 secs
    req = Request("http://www.fifa.com" + item, headers={'User-Agent': 'Mozilla/5.0'}) 
    webpage = urlopen(req).read()   #read the page


    page_soup = BeautifulSoup(webpage, "html.parser") #parse the site
    # order_list = page_soup.find_all("div", {"class": "ph-lnd-12 figure i-wrap "}) #extract anchor tags with class link-wrap and href is true
    order_list = page_soup.find_all("img", {"class": ["i-lnd-12", "i-lnd-stream-desktop"]}) #extract anchor tags with class link-wrap and href is true
    # import pdb; pdb.set_trace()

    for item in order_list:
        print(item['src'])
