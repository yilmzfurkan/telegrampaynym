#!/usr/bin/env python3
from lxml import html
import requests

name = input("Name of the Paynym? ")

page = requests.get('https://paynym.is/+' + name)
tree = html.fromstring(page.content)

paynymcode = tree.xpath('//span[@class="paycode"]/text()')

if len(paynymcode) == 1:
	print (*paynymcode)
else:
	print("No PayNym Found")