from bs4 import BeautifulSoup
import requests
import csv

#source=requests.get('http://coreyms.com')
#print(source) #only return code like 404 , 200

#The best way to open a local file with BeautifulSoup is to pass it an open file handler directly.
f_html=open('simple.html','r') #file from filehandling
soup=BeautifulSoup(f_html,'lxml') #return an object which represent the documment as a nested data structure

#print(soup.prettify())
print(soup.title)
print(soup.title.text)
print("\n")

for article in soup.find_all('div',class_='article'):
    print(article.h2.a.text)
    print(article.p.text)
    print("\n")
