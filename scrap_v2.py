#Importing all the necessary packages
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

#Url from which we scrape the data
url = "https://so2k19.wordpress.com/"

#Requests the web-page to open and store it in the variable
request_html = urlopen(url)
html_page = request_html.read()
request_html.close()

#Use BeautifulSoup to present the scrapped data properly
soup_html = soup(html_page, "html.parser")

#Find all the li elements where qoutes are present
content = soup_html.findAll('header', {'class','entry-header'})

file = open('blogpost.txt', 'w')

#Scrape the div for qoutes and authors and write it to the file
for data in content:
    title = data.find('h1', {'class','entry-title'}).text
    date = data.find('time', {'class','entry-date'}).text
    file.write("Blog-Title: "+title+"\nDate: "+date)
    file.write("\n \n")

file.close()
