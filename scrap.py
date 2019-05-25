#Importing all the necessary packages
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

#Url from which we scrape the data
url = "http://quotes.toscrape.com/"

#Requests the web-page to open and store it in the variable
request_html = urlopen(url)
html_page = request_html.read()
request_html.close()

#Use BeautifulSoup to present the scrapped data properly
soup_html = soup(html_page, "html.parser")

#Find all the div where qoutes are present
content = soup_html.findAll('div', {'class','quote'})

file = open('data.txt', 'w')

#Scrape the div for qoutes and authors and write it to the file
for data in content:
    quote = data.find('span', {'class','text'}).text
    author = data.find('small', {'class','author'}).text
    file.write("Qoute: "+quote+"\nAuthor: "+author)
    file.write("\n \n")

file.close()
