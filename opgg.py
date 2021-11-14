from bs4 import BeautifulSoup
import time
import requests
import webbrowser as wb

def retrieve_html(url):
        time.sleep(5)
        page = requests.get(url)
        
        return page 


def getopgg(url):
    html= retrieve_html(url)
    team1=[]
    team2=[]
    opgg1 = "https://euw.op.gg/multi/query="
    opgg2 = "https://euw.op.gg/multi/query="
    soup=BeautifulSoup(html.text,'html.parser')
    team1divs = soup.find("div", attrs={"class": "size-1-of-2 mobile-size-full"}).find_all("div", attrs={"class","text standard small summoner_player_id"})
    for div in team1divs:
        summoner=str(div.text)
        summoner=summoner.replace("Summoner Name","").replace(" ","").replace(":","").replace("Ansprechpartner","").replace("\n","")
        team1.append(summoner)
    
    team2divs = soup.find("div", attrs={"class": "size-1-of-2 mobile-size-full"}).find_next_sibling().find_all("div", attrs={"class", "text standard small summoner_player_id"})
    for div in team2divs:
        summoner = str(div.text)
        summoner = summoner.replace("Summoner Name", "").replace(" ", "").replace(
            ":", "").replace("Ansprechpartner", "").replace("\n", "")
        team2.append(summoner)
    opgg1=opgg1+team1[0]
    opgg2=opgg2+team2[0]
    
    for summoner in team1:
        opgg1=opgg1+"%2C"+summoner
    for summoner in team2:
        opgg2 = opgg2+"%2C"+summoner
    wb.open_new_tab(opgg2)
    wb.open_new_tab(opgg1)


getopgg(input("Link zur Playerseite eines Matches von Toornament:\n"))
