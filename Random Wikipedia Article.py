#my englesh not good I am sory If there are spelling errors 
#Run the commaind python -m pip install requests
import requests 
#Run the commaind pip install bs4
from bs4 import BeautifulSoup
#Not staps to this
import webbrowser
#This if 1 the comds loops if not conds not lops
i = 1
def TheCode():
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
    if Data_of_need_url == 'y':
        #This for show URL
        print('This url ', article_page.url)
        #This for ueser need pley comainds again
        Play_agian = input('Play again (y/n)')
        if Play_agian == 'y':
            #if write "y"pley again the comands  
            i = 1
     #This for not waint red to article       
    elif Data_of_need_url == 'n':
         Play_agian = input('Play again (y/n)')
         if Play_agian == 'y':
            #if write "y"pley again the comands  
             i = 1
    else:
        print('plese write (y/n)')
#This for loop the cominds              
while i == 1:
    i = 0
    TheCode()
