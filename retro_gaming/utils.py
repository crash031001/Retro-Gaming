import requests
from bs4 import BeautifulSoup

def get_rating(titulo):
    
    titulo_url = titulo.replace('-','').replace(' ','-').lower().replace('(','').replace(')','')
    titulo_url_sin_comilla = titulo_url.replace('´','').replace(':','').replace('/','-').replace('.','').replace(',','').replace('%','-')
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
  }
    url = f"https://metacritic.com/game/{titulo_url_sin_comilla}"   
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
      soup = BeautifulSoup(response.content, 'html.parser')
      rating_element = soup.find('div',class_="c-productScoreInfo_scoreNumber u-float-right")
      if rating_element:
        return rating_element.text
    return None
