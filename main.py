# If you want to scrape a website
# 1. Use the API
# 2. HTML web scraping using some tools like bs4

# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://internshala.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent) #--- the content of url in html format

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

# Step 3: HTML tree traversal
#
# Commonly used types of objects :
# 1. Tag ---- print(type(title))
# 2. NavigableString ---- print(type(title.string))
# 3. BeautifulSoup ---- print(type(soup))
# 4. Comment

# 4. Comment
# markup = "<p><!-- This is a comment --><p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p)
# print(soup2.p.string)
# print(type(soup2.p.string))
# exit()

# Get the title of html page
title = soup.title
#print(title)

# Get all the paragraphs from the page
paras = soup.find_all('p')
#print(paras)

#print(anchors)

#print(soup.find('p')) ---- The first paragrap of the web page
#print(soup.find('p')['class']) --- Get all the classes of the first p tag

# find all the elements with class lead
# print(soup.find_all("p", class_="mt-2"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())
#print(soup.get_text()) --- To get all the text only from the web page


# Get all the anchor Tags from the page
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page
"""for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://internshala.com"+link.get('href')
        all_links.add(link)
        # print(linkText)"""

# .contents - A tag's children are available as a list (store in memory)
# .children - A tag's children are available as a generator (not store in memory)
navbar = soup.find(class_='ham_main_heading')
for ele in navbar.contents:
    print(ele)

# Added FOR PROJECT

# for a_href in soup.find_all("a", href=True):
#    print(a_href["href"])


my_div = soup.find('div', class_='ham_main_heading')
link = my_div.find('a')['href']
clickable_link = f"<a href='{link}'>{link}</a>"
print(clickable_link)

# for item in navbar.strings:
#    print(item)

# for item in navbar.stripped_strings:
#    print(item)

#print(navbar.parent)

# for item in navbar.parents:
#    print(item.name)

# It take spaces also an element
# print(navbar.next_sibling.next_sibling)
# print(navbar.previous_sibling.previous_sibling) 

elem = soup.select('.title-font')
# print(elem)

