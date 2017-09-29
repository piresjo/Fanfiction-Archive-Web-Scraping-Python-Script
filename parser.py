import os
import requests
import time
from bs4 import BeautifulSoup
import re
import sys
import io
import argparse

parser = argparse.ArgumentParser(description='Parse Fanfiction')
parser.add_argument('header', type=str, nargs=1, help="header to actually scrape the files")
#parser.add_argument('-s', action='store_true', help='determine if we need to search for an actual header')
parser.add_argument('targetdir', type=str, nargs=1, help="place to put the scraped files")
args = parser.parse_args()
argv = vars(args)

header = argv['header'][0]
targetDir = argv['targetdir'][0]
myArray = []
resultList = ["start"]

# header =
# "http://archiveofourown.org/tags/Star%20Wars%20Episode%20VII:%20The%20Force%20Awakens%20(2015)/works?page="
# #can replace with url for any other fandom
end = 1

# insert target directory here
os.chdir(targetDir)

while (len(resultList)) != 0:
	page1 = requests.get(header + str(end))
	soup1 = BeautifulSoup(page1.text, "lxml")
	resultList = soup1(attrs={'href': re.compile('.*works/[0-9]+[0-9]$')})

	for x in resultList:
		body = str(x).split('"')
		docID = str(body[1]).split('/')
		page2 = requests.get("http://archiveofourown.org/" +
								 body[1] + "?view_adult=true&view_full_work=true")
		filename = str(docID[2]) + '.html'
		# Is encoding only in Python 3?
		f = open(filename, 'w', encoding='UTF')

		f.write(str(page2.text))
		f.close()
		print("reached document " + str(docID[2]) + " on page " + str(end))

		time.sleep(1)
		end += 1
