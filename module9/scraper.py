"""
Program: scraper.py
Author: Rachael Wolf
Last date modified: 10/25/2020

the purpose of this program is to get html data from a page in the dmacc calendar, store the
html in a text document, and print an easier to read version of the text.
"""
import requests
import bs4 as bs


url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=201903&Campus=1;4&S'
response = requests.get(url)
html = response.content
f = open("requestResult.txt", "w+")
f.writelines(str(html))
f.close()

soup = bs.BeautifulSoup(open("requestResult.txt"), 'html.parser')
print(soup.prettify())
