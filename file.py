#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:01:30 2019

@author: amandeepamandeep, Roja, Arvind
"""
#import request package for getting web data
import requests
#import beautifulsoup for web scrapping. Cool!
from bs4 import BeautifulSoup
#import pyodbc for connecting to azure
import pyodbc

# Connecting to Azure Server
server = ''
database = ''
username = ''
password = ''
#driver= '{ODBC Driver 17 for SQL Server}'
#cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
#to execute sql commands
#cursor = cnxn.cursor()

#getting data from page 
page = requests.get('https://www.businessinsider.com/100-highest-grossing-movies-of-all-time-at-the-worldwide-box-office-2018-11#95-the-chronicles-of-narnia-the-lion-the-witch-and-the-wardrobe-2005-6')
#creating beautifulsoup object
soup = BeautifulSoup(page.text,'html.parser')

#creating lists
movies = []
money = [] 
movies.clear
money.clear

#getting names of movie names that are in tag class 'slide-title-text'
movie_name_list = soup.find_all(class_='slide-title-text')
print(movie_name_list)
#iterating over the movie names object and extracting name
for movie_name in movie_name_list:
    movie = movie_name.contents[0]
    movies.append(movie)
    print(movie)
 
#getting worlwide grossing from strong tag
for strong in soup.find_all('strong'):
    if "World" in strong.contents[0]:
        mon = strong.next_sibling
        money.append(mon)
        print(mon)
#print(money.count)
#print(movies.count)
i=0
#cursor.execute("DECLARE @techonthenet VARCHAR(50)")
for item in movies:
    #saving data in azure server database table
    #cursor.execute("INSERT Movie (ID, movie_name, grossings) OUTPUT INSERTED.movie_name VALUES (?, ?, ?)", (i+1,item, money[i]))
    #cnxn.commit()
    if i < len(money)-1:
        i=i+1
