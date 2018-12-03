# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 12:12:59 2018

@author: G
"""

import xml.etree.cElementTree as ET

obj = ET.ElementTree(file='IT00410710586_1NRZM_EC_001.XML')
for elem in obj.iterfind('FatturaElettronicaHeader/DatiTrasmissione/IdTrasmittente/IdPaese'):
    print elem.text
