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
      categories ={'weather:weather':None,'wit$location:location':None}
      entity = list(resp['entities'])
      for en in entity:
        categories[en] =resp['entities'][en][0]['value']
      
    except:
        pass
    return categories

from pyowm import OWM

def get_news_elements(categories):

    owm = pyowm.OWM('43293d2e801bcd8a23955fad181b5d54')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(categories['wit$location:location'])
    w = observation.weather
    if categories['weather:weather']=='temperature':
        return w.temperature('celsius')['temp']
    elif categories['weather:weather']=='humidity':
        return w.humidity
    elif categories['weather:weather'] == 'rainfall':
        return w.rain


#message_text ="show me rains in Paris"

#print(get_news_elements(wit_response(message_text)))
