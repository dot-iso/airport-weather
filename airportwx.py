# Import Libraries
import sys
import urllib3
from bs4 import BeautifulSoup

def main(airport):
	# Specify URL
	airport_page = 'http://www.airnav.com/airport/' + airport

	# Query the webpage and return the html
	http = urllib3.PoolManager()
	page = http.request('GET', airport_page)

	# Parse
	soup = BeautifulSoup(page.data, 'html.parser')

	# Find the METAR out of the HTML
	html_string = 'body > table:nth-child(8)'
	find = soup.find(string="METAR").find_next('tr').find_next('table').find_next('tr').text

	# Output the METAR
	print(find)

if __name__ == "__main__":
	main(sys.argv[1])