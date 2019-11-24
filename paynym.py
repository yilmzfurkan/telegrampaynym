#!/usr/bin/env python3
from lxml import html
import requests
from requests import ConnectionError

try:
	name = input("Name of the Paynym?: ")
	page = requests.get('https://paynym.is/+' + name)
	tree = html.fromstring(page.content)
except ConnectionError:
	print("The website doesn't respond. ")
except KeyboardInterrupt:
	print("Nothing has been typed. ")

try:
	paynymcode = tree.xpath('//span[@class="paycode"]/text()')

	if len(paynymcode) == 1:
		print(*paynymcode)
	else:
		print("No PayNym found. ")

except NameError:
	pass
