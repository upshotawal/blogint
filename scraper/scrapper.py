
from email import header
from warnings import catch_warnings
from wsgiref import headers
import requests
from bs4 import BeautifulSoup



title = []
description = []
readtime = []
designation = []
authorname = []
images = []

url = 'https://proshore.eu/resources/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

r = requests.get(url, headers=headers)


# print(r.status_code)

soup = BeautifulSoup(r.content, features='lxml')

articles = soup.find_all('div', class_='playground-item-col')

for item in articles:
   
    title = item.find('h4', class_='playground-title').text.strip()
    

    description = item.find('div', class_='playground-excerpt').text.strip()
    readtime = item.find(
        'span', class_='playground-read-time-text').text.strip()
    designation = item.find(
        'div', class_='playground-author-description').text.strip()
    authorname = item.find('div', class_='playground-author-name').text.strip()
    images = item.findAll('img')
    example = images[0]
    links = example.attrs['src']

    print(title, description, readtime, designation, authorname, links)
