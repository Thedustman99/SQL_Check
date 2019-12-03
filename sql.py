# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 03:10:17 2019

@author: soura
"""

import requests


#domain = "https://hack-yourself-first.com/CarsByCylinders?Cylinders=V8"

def checkSql(domain):
    
    payloads = ("'", "'@", "';", '"', '")', '";', '$' ,'`', '`)', '`;', '--', "%27", "%25%27", "%60", "%5C")
    for payload in payloads:
        website = domain + "?" + payload
        print(website)
        result = requests.get(website)
        val = result.status_code
        if val == 200:
            print('Not vulnerable')
        elif val == 400:
            print('Client Error')
            break
        elif val == 500:
            print('Internal Server Error')
            break