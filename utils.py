# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:24:36 2021

@author: nibed
"""

from wit import Wit 
from gnewsclient import gnewsclient

access_token = "JXWWNT4S7EM7JI6FGPM526SPMHZXGTTB"

client = Wit(access_token = access_token)

def wit_response(message_text):
	resp = client.message(message_text)
	categories = {'newstype:newstype':None, 'wit$location:location':None}

	
	entities = list(resp['entities'])
	for entity in entities:
		categories[entity] = resp['entities'][entity][0]['value']
	
	return categories


def get_news_elements(categories):
	news_client = gnewsclient()
	news_client.query = ''

	if categories['newstype:newstype'] != None:
		news_client.query += categories['newstype:newstype'] + ' '

	if categories['wit$location:location'] != None:
		news_client.query += categories['wit$location:location']

	news_items = news_client.get_news()

	elements = []

	for item in news_items:
		element = {
					'title': item['title'],
					'buttons': [{
								'type': 'web_url',
								'title': "Read more",
								'url': item['link']
					}],
					'image_url': item['img']		
		}
		elements.append(element)

	return elements
