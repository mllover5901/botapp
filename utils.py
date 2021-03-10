# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:58:09 2021

@author: nibed
"""

from wit import Wit

access_token = "PZCGLHDPZB2GKN4A6VMORDT6KX6QR74M"

client = Wit(access_token = access_token)

def wit_response(message_text):
    resp = client.message(message_text)
    entity=None
    value = None
    try:
      val=[]
      
      entity = list(resp['entities'])
      for en in entity:
        
        value = resp['entities'][en][0]['value']
        val.append(value)
    except:
        pass
    return (entity,val)

#message_text ="show me the rainfall in Paris"

#print(wit_response(message_text))

