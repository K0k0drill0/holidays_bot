import requests 
import os
from bs4 import BeautifulSoup

url = 'https://kakoysegodnyaprazdnik.ru'
headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

def get_soup(url, headers):
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    soup = BeautifulSoup(resp.text, "html.parser")
    return soup

def div_args_checker(div_tag):
    if (div_tag.has_attr('itemprop') == False):
        return False
    return div_tag['itemprop'] == 'suggestedAnswer' or div_tag['itemprop'] == 'acceptedAnswer'

if __name__ == "__main__":
    f = open("hlds.txt", "w+", encoding="utf-8")
    soup = get_soup(url, headers)
    for div_tag in soup.find_all(div_args_checker):
        f.write(div_tag.span.string)
        f.write("\n")
