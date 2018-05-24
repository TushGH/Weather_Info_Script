# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 00:43:38 2017

@author: Tushar V Deshpande



********* References ***********
References: 
1) National Weather Service - National Digital Forecast Database (NDFD) Simple Object Access Protocol (SOAP) Web Service 
   retrived From - https://graphical.weather.gov/xml/ 
2) National Weather Service - XML Feeds of Current Weather Conditions
   retrived From - http://w1.weather.gov/xml/current_obs/
3) youtube.com Python Programming Tutorial - 24 - Downloading Files from the Web 
   retrived from - https://www.youtube.com/watch?v=MjwWzBiAMck
4) Geeks For Geeks  -XML Parsing
   retrived from - http://www.geeksforgeeks.org/xml-parsing-python/
5) Python software foundation - for The ElementTree XML API
   retrived from - https://docs.python.org/2/library/xml.etree.elementtree.html#finding-interesting-elements
6) Tutorials Point - for Xpath Query Examples 
   retrived from - https://www.tutorialspoint.com/xpath/xpath_expression.htmv
7) Python For Beginners [ Request Library In Python ]
   retrived from http://www.pythonforbeginners.com/requests/using-requests-in-python
   
"""

import requests   #import Request Library
import xml.etree.ElementTree as ET #import Xml Parser


"""
@Function: loadRSS
@input : Latitude and Longitude
This Function Takes The Latitude and Longitude of a location and finds the
appropriate Xml File for the weather information . Pass This TO display function
"""
def loadRSS(latitude1 , longitude1):
    url11 = 'http://w1.weather.gov/xml/current_obs/index.xml' # Refer to Reference 2
    
    #  print The location detail
    print(latitude1)
    print(longitude1)
    # creating HTTP response object from given url
    resp = requests.get(url11)
    # saving the xml file
    with open('mainweatherdata.xml', 'wb') as f:
        f.write(resp.content)
    #parse the xml file and get he root of xml file
    
    tree = ET.parse('mainweatherdata.xml')
    root = tree.getroot()
    abc = root.findall("station")
    print("successful xml retrived , if Info Dosent exit please check the Location Details")
    # serach for the specific station and pass the value of xml_url to display function.
    for a in abc :
            if(a.find('latitude').text ==latitude1 and a.find('longitude').text == longitude1):
                data_url = a.find('xml_url').text
                print(data_url)
                display(data_url)
               
        
"""
@Function : display
@input : Xml_Url 
This Function parse the Xml downloaded from the url and displays the weather information
"""       
def display(data_url):
     # creating HTTP response object from given url
    response = requests.get(data_url) 
    
    with open('data.xml', 'wb') as f:
        f.write(response.content)
   
    #parse the xml file and get he root of xml file
    tree2 = ET.parse('data.xml')
    root = tree2.getroot()
    #display weatherInformation
    try:
        print('***********************************************************')
        print('***************WEATHER REPORT******************************')
        print('The Location is  ' ,root.find("location").text )
        print('Temperature' ,root.find("temperature_string").text)
        print('Relative Humidity ' ,root.find("relative_humidity").text )
        print('Wind String ' ,root.find("wind_string").text )
        print('dewpoint  ' ,root.find("dewpoint_f").text )
        print('pressure_string ' ,root.find("pressure_string").text )
        
        print('***********************************************************')
    except AttributeError :
        pass
    
"""
This function Takes the Location information from User
"""    
def UserInput():
    Longitude = input("Enter The Longitude ")
    latitude = input ("Enter The latitude ")
    loadRSS(Longitude , latitude)
    

#Call The UserInput Function
UserInput()
