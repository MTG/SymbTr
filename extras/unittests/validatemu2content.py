# -*- coding: utf-8 -*-
from symbtrdataextractor import symbtrreader
from fileoperations.fileoperations import getFileNamesInDir

import os

def test_mu2_header_rows():
	col_names = {2:u'Pay', 3:u'Payda', 4:u'Legato%', 5:u'Bas', 
		6:u'Cek', 7:u'Soz-1', 8:u'Soz-2'}
	is_headers_correct = True

	[mu2filepaths, mu2folders, mu2names] = get_mu2_filenames()

	for mf, mn in zip(mu2filepaths, mu2names):
		header_row = symbtrreader.readMu2HeaderRow(mf)
		
		for ii in range(0, len(col_names) + 1):
			if ii in [0, 1]:
				try: 
					dummyint = int(header_row[ii])
				except ValueError:  # not int
					is_header_correct = False
					print mn + ': ' + str(ii) + 'th column in the header row should have been an integer!'
			elif ii == len(col_names) + 1:
				try: 
					dummyfloat = float(header_row[ii])
				except ValueError:  # not float
					is_header_correct = False
					print mn + ': ' + str(ii) + 'th column in the header row should have been a float!'
			else:
				pass
				if not header_row[ii] == col_names[ii]:
					is_header_correct = False
					print u'%s: %dth column in the header row should have been named "%s" instead of "%s"' % (
						mn, ii, col_names[ii], header_row[ii])

	assert is_headers_correct

def get_mu2_filenames():
	symbTrMu2folder = './mu2/'
	return getFileNamesInDir(symbTrMu2folder, keyword = '*.mu2')