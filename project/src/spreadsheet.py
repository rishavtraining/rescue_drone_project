'''
* Project Name: Unmanned Aerial System for flood disaster emergency response 
                and rescue management

* Author List: Krishna Nimbalkar

* Filename: spreadsheet.py

* Functions: initializeData(),sendData(),clearData()

* Global Variables: index

'''
#########################################################################
#   Author @          Krishna Nimbalkar                                 #
#   Created On :      27/11/2020                                        #
#   Last Modified :   27/11/2020                                        #
#   Description :     This Python program to read, write, and delete    #
#                     data from a Google Spreadsheet                    #
#########################################################################

# ref link : https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
#            https://gspread.readthedocs.io/en/latest/
# This project is under test-app
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import random
from datetime import datetime
import time


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("droneProject").sheet1

# Extract and print all of the values
#list_of_hashes = sheet.get_all_records()
#pprint(list_of_hashes)

index = 0


def initializeData():

    clearData()
    global index
    # Insert a row in the spreadsheet:
    row = ["id","time","people","longitude","latitude"]
    sheet.insert_row(row, 1)
    index = 2


def sendData(people,longitude,latitude):

    global index
    print("index : ",index)
    if index == 1 or index == 0:
        initializeData()
    uid = index
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    row = [uid,time,people,longitude,latitude]
    sheet.insert_row(row, index)
    index = index + 1
    
#id 	time	people	longitude	latitude

def clearData():

    global index
    print("clearing data in worksheet")
    sheet.clear()
    index = 0
    print("index : ",index)
    
clearData()

