# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:27:09 2018

@author: G
"""

import pandas as pd
import sqlalchemy
import pymysql


dati=pd.read_csv('Conferimento_Fondi_Svalutazione_load.csv', header=[0], sep=';')

engine=sqlalchemy.create_engine('mysql+pymysql://root:pica489sso@localhost:3306/test')

dati.to_sql(
     name='svalut_ini',
     con=engine,
    index=False,
    if_exists='append'
)


