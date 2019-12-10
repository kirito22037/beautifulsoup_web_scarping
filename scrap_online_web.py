import csv
from bs4 import BeautifulSoup
import requests

source=requests.get('http://coreyms.com').text
soup=BeautifulSoup(source,'lxml')

#print(soup.title)

filehand_csv=open('csv_file.csv','w')  #open file by filehandling in write mode

csv_writer=csv.writer(filehand_csv)  #the filehandling file is opend by csv file handler to be written

csv_writer.writerow(['headline','summary','videolink'])  #write the column names in 1st row

for article in soup.find_all('article'):

        headline=article.header.text
        print(headline)

        summary=article.find('div',class_='entry-content').p.text
        print(summary)

        try:
            videolink=article.iframe['src']         #we can access attribute of elemnt by passing attribue as a keyword in dictionary
            videolink=videolink.split('/')
            videolink=videolink[4]


        #except:
        #    videolink=article.find('div',class_='wp-block-embed__wrapper').text
        #    videolink=videolink.split('/')
        #    videolink=videolink[3]

        except Exception as e:
            videolink=None

        videolink = f'https://youtube.com/watch?v={videolink}'
        print(videolink)

        print("\n")

        csv_writer.writerow([headline,summary,videolink])     #write the data in comma seprated row

filehand_csv.close()
