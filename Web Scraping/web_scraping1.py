import requests
from bs4 import BeautifulSoup
import csv

url = 'https://coreyms.com/'

source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

title = soup.title.text
# print('The title of the website is:', title)

# scrap each article's link, headline, paragraph, and video link
articles = soup.find_all('article')

# to save the data into a csv file
csvfile = open('hendy.csv', 'w', encoding='utf-8')
writer = csv.writer(csvfile)
writer.writerow(['headline', 'link', 'paragraph', 'video link'])

for i in range(len(articles)):
    print('This is article '+str(i+1)+': ')

    headline = articles[i].header.h2.a.text
    print('The headline of article '+str(i+1)+' is '+headline)

    link = articles[i].a.attrs['href']
    print(link)

    paragraph = articles[i].find('div', class_='entry-content').p.text
    print(paragraph)

    # prevents possible errors when some articles don't have videos
    try:
        video_link = articles[i].find('iframe', class_='youtube-player')['src']
        print(video_link)
        writer.writerow([headline, link, paragraph, video_link])
    except:
        writer.writerow([headline, link, paragraph])
csvfile.close()  # close the file
