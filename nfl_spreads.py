from bs4 import BeautifulSoup
import requests
import html5lib
import csv

url = "http://www.footballlocks.com/nfl_point_spreads.shtml"
page = requests.get(url)

soup = BeautifulSoup(page.content, features='html5lib')

favorite = []
underdog =[]
spread = {}
table_title = soup.find_all(string=["Favorite", "Underdog"])
table_data = soup.find_all(attrs={"width":580})

def find():

   search=input("Which team do you want to see? ")
   for data in table_data:
       if search == data:
           print("tr")

find()

if __name__ == "__main__":
    pass
