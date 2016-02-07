from urllib.request import Request, urlopen
import requests
import time

img_url_list = [
                "http://img.fifa.com/mm/photo/tournament/competition/02/40/53/48/2405348_xbig-lnd.jpg",
                "http://img.fifa.com/mm/photo/tournament/competition/01/27/31/84/1273184_xbig-lnd.jpg"
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/52/35/80/523580_full-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/52/31/28/523128_full-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/52/28/36/522836_xbig-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/52/24/45/522445_full-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/52/23/10/522310_big-lnd.jpg",
                # "http://img.fifa.com/mm/photo/classic/players/51/52/22/515222_xbig-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/52/09/07/520907_xbig-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/51/96/36/519636_xbig-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/51/84/93/518493_full-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/51/49/52/514952_full-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/51/95/02/519502_xbig-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/51/21/59/512159_full-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/51/51/42/515142_big-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/51/51/51/515151_full-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/51/23/07/512307_big-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/52/29/12/522912_big-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/52/29/16/522916_big-lnd.jpg",
                # "http://img.fifa.com/mm/photo/archivedtournament/summaries/52/31/19/523119_big-lnd.jpg"
]
start = 2014
for item in img_url_list:
    time.sleep(3) #sleep for 3 secs

    r = requests.get(item)
    with open(str(start) + "_poster.jpg", 'wb') as outfile:
        outfile.write(r.content)

    start -= 4
