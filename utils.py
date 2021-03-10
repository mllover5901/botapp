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
	
	entity = None
	value = None

	try:
		entity = list(resp['entities'])[0]
		value = resp['entities'][entity][0]['value']
	except:
		pass

	return (entity, value)
