###################################
# computerModelCrawler.py         #
# Grabs and stores information    #
# about different computer models #
# parsed from LappyList           #
###################################

from BeautifulSoup import BeautifulSoup
import pdb
import os
# Use this if you have a javascript based scraper installed
# sites = {'gaming': 'http://www.lappylist.com/laptops/best-gaming-laptops/', 'ultraportable': 'http://www.lappylist.com/laptops/best-ultraportable-laptops/', 'convertibles': 'http://www.lappylist.com/laptops/best-convertible-laptops/', 'programming': 'http://www.lappylist.com/laptops/best-programming-laptops/', 'mainstream': 'http://www.lappylist.com/laptops/best-mainstream-laptops/'}

# Use this for the static files
sites = {'gaming': 'gaming.html', 'ultraportable': 'ultraportable.html', 'convertibles': 'convertibles.html', 'programming': 'programming.html', 'mainstream': 'mainstream.html'}

allModels = []

for key, value in sites.iteritems():
	print "Getting information for " + key + " computers"
	with open(os.path.dirname(os.path.realpath(__file__)) + '/static/crawledSites/' + key + '.html', 'r') as compHTML:
		html = compHTML.read()
		soup = BeautifulSoup(html)
		compTable = soup.find('table', id="lappylist-table")
		rows = compTable.findAll('tr')[1:-1]
		for row in rows:
			iterData = []
			for td in row.findAll('td'):
				if td.find('a'):
					iterData.append(td.find('a').text)
				else:
					iterData.append(td.text)
			allModels.append(iterData)

print allModels
