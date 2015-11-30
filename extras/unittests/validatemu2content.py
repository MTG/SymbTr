# -*- coding: utf-8 -*-
from symbtrdataextractor import symbtrreader
from fileoperations.fileoperations import getFileNamesInDir

import os

def test_mu2_header_rows():
	col_names = {2:u'Pay', 3:u'Payda', 4:u'Legato%', 5:u'Bas', 
		6:u'Çek', 7:u'Söz-1', 8:u'Söz-2'}	
	
	numErrors = 0

	[mu2filepaths, mu2folders, mu2names] = get_mu2_filenames()

	for mf, mn in zip(mu2filepaths, mu2names):
		header_row = symbtrreader.readMu2Header(mf)[1]
		
		for ii in range(0, len(col_names) + 1):
			if ii in [0, 1]:
				try: 
					dummyint = int(header_row[ii])
				except ValueError:  # not int
					numErrors += 1
					print mn + ': ' + str(ii) + 'th column in the header row should have been an integer!'
			elif ii == len(col_names) + 1:
				try: 
					dummyfloat = float(header_row[ii])
				except ValueError:  # not float
					numErrors += 1
					print mn + ': ' + str(ii) + 'th column in the header row should have been a float!'
			else:
				if not header_row[ii] == col_names[ii]:
					numErrors += 1
					print u'%s: %dth column in the header row should have been named "%s" instead of "%s"' % (
						mn, ii, col_names[ii], header_row[ii])

	if numErrors > 0:
		print ''
		print '%d errors in mu2 file header rows' %numErrors
	assert numErrors == 0 

def get_mu2_filenames():
	symbTrMu2folder = './mu2/'
	return getFileNamesInDir(symbTrMu2folder, keyword = '*.mu2')