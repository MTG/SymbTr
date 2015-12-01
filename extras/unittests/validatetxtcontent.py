from symbtrdataextractor import extractor
from fileoperations.fileoperations import getFileNamesInDir

import os

def test_txt_data():
	[txtfilepaths, txtfolders, txtnames] = get_txt_filenames()

	isAllDataValid = True
	for tf, tn in zip(txtfilepaths, txtnames):
		txtdata, isDataValid = extractor.extract(tf)
		isAllDataValid = isDataValid if isAllDataValid else False

	assert(isAllDataValid)

def get_txt_filenames():
	symbTrTxtfolder = './txt/'
	return getFileNamesInDir(symbTrTxtfolder, keyword = '*.txt')