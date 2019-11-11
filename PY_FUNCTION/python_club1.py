# http://localhost:8888/?token=adf4e13cd0538178b6ee1dfeb4a20f624f301983cb360f8d
# pip install requests_html
# github.com/mrbenjones/requests_demos/tree/master/requests
# treyHunter: assigns programs // gives you unit-tests
from requests_html import HTMLSession
site="https://www.meetup.com/AbqPython/"
session = HTMLSession()
r = session.get(site)

cards = r.html.find(".dateDisplay")
for card in cards:
    print(card.text)
    print("---")
