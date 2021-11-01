from bs4 import BeautifulSoup
import requests
import html5lib
import csv

url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html5lib")

print(soup)

if __name__ == "__main__":
    pass
