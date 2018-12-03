# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:08:03 2018

@author: G
"""

import requests

user_agent_url = 'http://www.user-agents.org/allagents.xml'
xml_data = requests.get(user_agent_url).content

from XML2DataFrame import XML2DataFrame


xml2df = XML2DataFrame(xml_data)
xml_dataframe = xml2df.process_data

print(xml_dataframe)
