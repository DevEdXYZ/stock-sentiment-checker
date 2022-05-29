import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import colorama
from colorama import Fore, Back, Style
import time
import sys
colorama.init()





print(Fore.RED + """

 _____ _             _                       _   _                      _            _               _             
/  ___| |           | |                     | | (_)                    | |          | |             | |            
\ `--.| |_ ___   ___| | __    ___  ___ _ __ | |_ _ _ __ ___   ___ _ __ | |_      ___| |__   ___  ___| | _____ _ __ 
 `--. \ __/ _ \ / __| |/ /   / __|/ _ \ '_ \| __| | '_ ` _ \ / _ \ '_ \| __|    / __| '_ \ / _ \/ __| |/ / _ \ '__|
/\__/ / || (_) | (__|   <    \__ \  __/ | | | |_| | | | | | |  __/ | | | |_    | (__| | | |  __/ (__|   <  __/ |   
\____/ \__\___/ \___|_|\_\   |___/\___|_| |_|\__|_|_| |_| |_|\___|_| |_|\__|    \___|_| |_|\___|\___|_|\_\___|_|   
                                                                                                                   
                                                                                                                   
""")

time.sleep(2)
print(Fore.BLUE + "-----------------------------------------------------")

print(Fore.MAGENTA + "Input a ticker symbol to get the sentiment value")
print(Fore.YELLOW + """this supports any ticker but here are a few to try""")
print (Fore.WHITE + """
AAPL
MSFT
GOOG
GOOGL
AMZN
FB
TSLA
BRL.A
BRK.B
TSM
NVDA
V
JPM
BABA""")
print(Fore.BLUE + "-----------------------------------------------------")



if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen

cpositive_score = 0
cnegative_score = 0
positive_score = 0
negative_score = 0
positive_list = []
negative_list = []
text_list = []

f1 = open ("positive words.txt")
input1 = f1.read()
positive = input1.split()


f2=open("negative words.txt")
input1 = f2.read()
negative = input1.split()

for word in positive:
    positive_list.append(word)




for word in negative:
    negative_list.append(word)





###################################################################



from bs4 import BeautifulSoup as bs
import requests_html

######################################################################################
######################################################################
######################################################################
#########################community
######################################################################
######################################################################

x = input(Fore.RED+"enter ticker symbol: ")
print(Fore.BLUE + "-----------------------------------------------------")

print ("getting community scores")
print("---------------------------")

print ("getting " + x + " score from Yahoo")
print("---------------------------")

s = requests_html.HTMLSession()
page = s.get('https://uk.finance.yahoo.com/quote/{x}/community')
soup=bs(page.text,'lxml')
text = (soup.get_text())
text = text.split()


for word in text:
    text_list.append(word)



for word in text_list:
    temp = word.lower()
    for _ in positive_list:
        if temp == _.lower():
            cpositive_score = cpositive_score + 1

for word in text_list:
    temp = word.lower()
    for _ in negative_list:
        if temp == _.lower():
            cnegative_score = cnegative_score + 1



print ("getting " + x + " score from Reddit")
print("---------------------------")
s = requests_html.HTMLSession()
page = s.get('https://www.reddit.com/search/?q={x}')
soup=bs(page.text,'lxml')
text = (soup.get_text())
text = text.split()


for word in text:
    text_list.append(word)



for word in text_list:
    temp = word.lower()
    for _ in positive_list:
        if temp == _.lower():
            cpositive_score = cpositive_score + 1

for word in text_list:
    temp = word.lower()
    for _ in negative_list:
        if temp == _.lower():
            cnegative_score = cnegative_score + 1

print ("getting " + x + " score from Quora")
print("---------------------------")


s = requests_html.HTMLSession()
page = s.get('https://www.quora.com/search?q={x}&time=week')
soup=bs(page.text,'lxml')
text = (soup.get_text())
text = text.split()


for word in text:
    text_list.append(word)



for word in text_list:
    temp = word.lower()
    for _ in positive_list:
        if temp == _.lower():
            cpositive_score = cpositive_score + 1

for word in text_list:
    temp = word.lower()
    for _ in negative_list:
        if temp == _.lower():
            cnegative_score = cnegative_score + 1


print ("getting " + x + " score from Twitter")
print("---------------------------")

s = requests_html.HTMLSession()
page = s.get('https://twitter.com/search?q={x}&src=typed_query&f=top')
soup=bs(page.text,'lxml')
text = (soup.get_text())
text = text.split()


for word in text:
    text_list.append(word)



for word in text_list:
    temp = word.lower()
    for _ in positive_list:
        if temp == _.lower():
            cpositive_score = cpositive_score + 1

for word in text_list:
    temp = word.lower()
    for _ in negative_list:
        if temp == _.lower():
            cnegative_score = cnegative_score + 1

######################################################################################
######################################################################
######################################################################
#########################NEWS
######################################################################
######################################################################


print ("getting news scores")
print("---------------------------")

print ("getting " + x + " score from Yahoo")
print("---------------------------")

s = requests_html.HTMLSession()
page = s.get('https://uk.finance.yahoo.com/quote/{x}')
soup=bs(page.text,'lxml')
text = (soup.get_text())
text = text.split()


for word in text:
    text_list.append(word)



for word in text_list:
    temp = word.lower()
    for _ in positive_list:
        if temp == _.lower():
            positive_score = positive_score + 1

for word in text_list:
    temp = word.lower()
    for _ in negative_list:
        if temp == _.lower():
            negative_score = negative_score + 1




###############################################################################################
print ("getting " + x + " score from MarketWatch")
print("---------------------------")

page = s.get("https://www.marketwatch.com/investing/stock/{x}")
soup=bs(page.text,'lxml')
text = (soup.get_text())
text = text.split()


for word in text:
    text_list.append(word)



for word in text_list:
    temp = word.lower()
    for _ in positive_list:
        if temp == _.lower():
            positive_score = positive_score + 1

for word in text_list:
    temp = word.lower()
    for _ in negative_list:
        if temp == _.lower():
            negative_score = negative_score + 1

print ("getting " + x + " score from Cnbc")


page = s.get("https://www.cnbc.com/quotes/{x}?tab=news")
soup=bs(page.text,'lxml')
text = (soup.get_text())
text = text.lower()
text = text.split()


for word in text:
    text_list.append(word)



for word in text_list:
    temp = word.lower()
    for _ in positive_list:
        if temp == _.lower():
            positive_score = positive_score + 1

for word in text_list:
    temp = word.lower()
    for _ in negative_list:
        if temp == _.lower():
            negative_score = negative_score + 1

print (Fore.BLUE +"--------------------------------")
print (str(cpositive_score) + Fore.GREEN + " community positive score")
print ("--------------------------------")
print (str(cnegative_score) + Fore.RED + " community negative score")
print (Fore.BLUE +"-----------------------------------------------------")

print (str(positive_score) + Fore.GREEN + " news positive score")
print (Fore.BLUE +"--------------------------------")
print (str(negative_score) + Fore.RED + " news negative score")
print(Fore.BLUE + "-----------------------------------------------------")


input("press enter to exit: ")

