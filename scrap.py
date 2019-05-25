from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

url = "http://quotes.toscrape.com/"

request_html = urlopen(url)

html_page = request_html.read()
request_html.close()

soup_html = soup(html_page, "html.parser")

content = soup_html.findAll('div', {'class','quote'})

file = open('data.txt', 'w')

for data in content:
    quote = data.find('span', {'class','text'}).text
    author = data.find('small', {'class','author'}).text
    file.write("Qoute: "+quote+"\nAuthor: "+author)
    file.write("\n \n")

file.close()