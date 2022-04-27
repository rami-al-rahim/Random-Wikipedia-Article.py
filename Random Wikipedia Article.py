#my englesh not good I am sory If there are spelling errors 
#Run the commaind python -m pip install requests
import requests 
#Run the commaind pip install bs4
from bs4 import BeautifulSoup
#Not staps to this
import webbrowser
   
#if opein url opein random article of wikipedia
url = 'https://en.wikipedia.org/wiki/Special:Random'
#Git th data of url 
article_page = requests.get(url)
#Stap the BeautifulSoup
soup = BeautifulSoup(article_page.text, 'html.parser')
#To git titrl name of Random wikipedia article
article_Titel = soup.find(id='firstHeading')
#Write article name on rain this file and you can rename the text of this("")
print('The tital of random article is', article_Titel.string)
#To Know the user need url and you can rename the text of this("")
Data_of_need_url = input('You wanit to rade this (y/n)')
if Data_of_need_url =="y":
    #This to Write the url 
    print('This url ', article_page.url)
    #If you want opein url delate this (#)
    #webbrowser.open_new_tab(article_page.url)\
    Play_agian = input('Play again (y/n)')
    if Play_agian == 'y':
        print('h')
elif Data_of_need_url == 'n':
    Play_agian = input('Play again (y/n)')
    if Play_agian == 'y':
        print('h')
else:
    Play_agian = print('Write (y/n) plese')
