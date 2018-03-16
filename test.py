#Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
 
# url of rss feed
url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'

# creating HTTP response object from given url
resp = requests.get(url)

# saving the xml file
with open('topnewsfeed.xml', 'wb') as f:
    f.write(resp.content)
         
 
# create element tree object
tree = ET.parse("topnewsfeed.xml")

# get root element
root = tree.getroot()

# create empty list for news items
newsitems = []

print(root)

# iterate news items
for item in root.findall('./channel/item'):

    # empty news dictionary
    news = {}
    print(item.tag, item.attrib)
    # iterate child elements of item
    for child in item:
        print(child.tag, child.attrib)
        # special checking for namespace object content:media
        if child.tag == '{http://search.yahoo.com/mrss/}content':
            news['media'] = child.attrib['url']
        else:
            news[child.tag] = child.text.encode('utf8')

    # append news dictionary to news items list
    newsitems.append(news)
     
