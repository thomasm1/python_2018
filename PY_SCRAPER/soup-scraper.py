# Description: Scrapes the AI-CIO website for news articles
from bs4 import BeautifulSoup
import requests
from datetime import datetime

def ParseUrl(url):
    try:
        req = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(req.content, 'lxml')
        last_page = soup.find(text="Next")
        if last_page is not None:
            page = last_page.find_previous('li').find_previous('li')
            page_url = ('https://www.ai-cio.com/news/page/' + page.a['href'].split('&')[0]+'&pg=')
            return [page_url+str(x) for x in range(1, int(page.text)+1)] 
        else:
            last_page = soup.find('a', class_='last').text
    except:
        return None
    
def Parse(url, data=[]):
    try:
        req = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(req.content, 'lxml')
        for article in soup.find_all('article', class_='news-item'):
            title = article.h2.text
            date = article.find('span', class_='date').text
            link = article.a['href']
            data.append({'title': title, 'date': date, 'link': link})
        return data
    except:
        return None