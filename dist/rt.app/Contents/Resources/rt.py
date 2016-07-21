"""This is a working example of a receiving report application"""
from easygui import *
import sys


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
	fieldNames = ['Lumber (ea)', 'Bricks (ea)', 'Concrete (ea)', 'Nails (ea)', 'Water Tank (ea)']
	fieldValues = []
	fieldValues = multenterbox(msg, title, fieldNames)

	while True:
		allareintegers = True
		for i in fieldValues:
			try:
				test = int(fieldValues[i])
			except: 
				allareintegeres = False

		if allareintegers == False:
			errmsg = 'Inputs must be numbers.'
			fieldValues = multenterbox(errmsg, title, fieldNames)
		else: 
			break
	return fieldValues

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



date, location = initialize()
	
lumber, bricks, concrete, nails, watertank = getitems()

finish(lumber, bricks, concrete, nails, watertank)
	
	