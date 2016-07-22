"""This is a working example of a receiving report application"""
from easygui import *
import sys
import smtplib
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials




def authgoogle():


	#connect to google
	scope = ['https://spreadsheets.google.com/feeds']

	credentials = ServiceAccountCredentials.from_json_keyfile_name('Receiving Reports-b234d394a35b.json', scope)

	gc = gspread.authorize(credentials)

	wks = gc.open("Item Codes").sheet1

	#test edit a cell
	wks.update_acell('F1', 'Python Edit Test Cell')

	return wks

def downloadrows():

	#get length of lists
	'''TOTO'''


	#grab lists
	code_list = wks.col_values(2)[3:132]
	item_list = wks.col_values(3)[3:132]
	uoms_list = wks.col_values(4)[3:132]

	#build list of lists
	masterlist = []

	for i in range(0, len(code_list)):
		minilist = []
		minilist.append(code_list[i])
		minilist.append(item_list[i])
		minilist.append(uoms_list[i])
		masterlist.append(minilist)

	print masterlist

	return item_list, masterlist




def initialize():
	msg = 'Would you like to create a new receiving report?'
	title = 'Receiving Report'
	if ccbox(msg, title):
		dothething = 1
		date, location = getdateandlocation()
		return date, location
	else:
		sys.exit(0)

def getdateandlocation():
	msg = 'Insert today\'s date and the receiving location'
	title = 'Receiving Report'
	fieldNames = ['Date', 'Location']
	fieldValues = []
	fieldValues = multenterbox(msg, title, fieldNames)

	while True:
		if fieldValues == None: break
		errmsg = ''
		for i in range(len(fieldNames)):
			if fieldValues[i].strip() == '':
				errmsg = errmsg + ('%s is a required field.\n\n' % fieldNames[i])
		if errmsg == '':
			break
		fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
	return fieldValues


def getitems():
	msg = 'Insert the quantity of items you are receiving'
	title = 'Receiving Report'
	fieldNames = item_list
	fieldValues = []
	fieldValues = multenterbox(msg, title, fieldNames)

	while True:
		allareintegers = True
		for i in range(0, len(fieldValues)-1):
			try:
				test = int(fieldValues[i])
			except:
				if fieldValues[i]=='':
					allareintegers = True
				else: allareintegers = False

		if allareintegers == False:
			errmsg = 'Inputs must be integers'
			fieldValues = multenterbox(errmsg, title, fieldNames)
		else:
			break
	return fieldValues

def finish(item_list, fieldValues):

	#initialize file and get location
	filename = 'export.csv'
	pathtofile = diropenbox('Where do you want to save your report?')
	pathtofile = '%s/%s' % (pathtofile, filename)
	export = open(pathtofile, "w")

	#remove all commas from the item_list
	for i in range(0, len(item_list)-1):
		item_list[i] = item_list[i].replace(',', ' ')

	#write strings to csv file
	for i in range(0, len(item_list)-1):
		export.write('%s, %s, %s, %s,' % (date, location, item_list[i], fieldValues[i]))
		export.write('\n')

	export.close()
	msgbox('You have finished! Check the working directory to find your CSV file')


'''

def finish(lumber, bricks, concrete, nails, watertank):
	string1 = '%s, %s, lumber, %s, ' % (date, location, lumber)
	string2 = '%s, %s, bricks, %s, ' % (date, location, bricks)
	string3 = '%s, %s, concrete, %s, ' % (date, location, concrete)
	string4 = '%s, %s, nails, %s, ' % (date, location, nails)
	string5 = '%s, %s, watertank, %s, ' % (date, location, watertank)
	filename = 'export.csv'
	pathtofile = diropenbox('Where do you want to save your report?')
	pathtofile = '%s/%s' % (pathtofile, filename)
	export = open(pathtofile, "w")
	export.write(string1 + '\n' + string2 + '\n' + string3 + '\n' + string4 + '\n' + string5)
	export.close()
	msgbox('You have finished! Check the working directory to find your CSV file')
'''



wks = authgoogle()
item_list, masterlist = downloadrows()
date, location = initialize()	

quantities = getitems()
finish(item_list, quantities)
	
	