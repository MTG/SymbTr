from fileoperations.fileoperations import get_filenames_in_dir

import os
import json
import subprocess

def test_score_numbers():
	(symbtrtxtnames, symbtrmu2names, symbtrpdfnames, 
		symbtrxmlnames, symbtrmidnames, symbtrjsonnames) = getsymbtrnames()

	print "Number of txt: " + str(len(symbtrtxtnames))
	print "Number of mu2: " + str(len(symbtrmu2names))
	print "Number of pdf: " + str(len(symbtrpdfnames))
	print "Number of MusicXML: " + str(len(symbtrxmlnames))
	print "Number of midi: " + str(len(symbtrmidnames))
	print "Number of mbid relations: " + str(len(symbtrjsonnames))

	assert all([len(symbtrtxtnames) == len(symbtrmu2names),
		len(symbtrmu2names) == len(symbtrpdfnames),
		len(symbtrpdfnames) == len(symbtrxmlnames),
		len(symbtrxmlnames) == len(symbtrmidnames),
		len(symbtrmidnames) == len(symbtrjsonnames)])

def test_score_names():
	(symbtrtxtnames, symbtrmu2names, symbtrpdfnames, 
		symbtrxmlnames, symbtrmidnames, symbtrjsonnames) = getsymbtrnames()

	assert all([len(setDiff(symbtrtxtnames, symbtrmu2names)) == 0, 
		len(setDiff(symbtrmu2names, symbtrpdfnames)) == 0, 
		len(setDiff(symbtrpdfnames, symbtrxmlnames)) == 0, 
		len(setDiff(symbtrxmlnames, symbtrmidnames)) == 0, 
		len(setDiff(symbtrmidnames, symbtrjsonnames)) == 0, 
		len(setDiff(symbtrjsonnames, symbtrtxtnames)) == 0])

def test_encoding():
	symbTrfolder = './'
	symbTrTxtfolder = os.path.join(symbTrfolder, 'txt/')
	symbTrMu2folder = os.path.join(symbTrfolder, 'mu2/')

	symbtrtxtfiles = get_filenames_in_dir(symbTrTxtfolder, keyword = '*.txt')[0]
	symbtrmu2files = get_filenames_in_dir(symbTrMu2folder, keyword = '*.mu2')[0]

	isallvalid = True
	for txt in symbtrtxtfiles:
		out = subprocess.check_output("file -i " + txt, shell = True)
		# If there are no "Turkish" characters in a file, the encoding will be
		# seen as us-ascii which is a subset of UTF-8
		if not any(charset in out for charset in ['utf-8', 'us-ascii']):
			print out
			isallvalid = False
			
	for mu2 in symbtrmu2files:
		out = subprocess.check_output("file -i " + mu2, shell = True)
		# If there are no "Turkish" characters in a file, the encoding will be
		# seen as us-ascii which is a subset of UTF-8
		if not any(charset in out for charset in ['utf-8', 'us-ascii']):
			print out
			isallvalid = False

	assert isallvalid

def getsymbtrnames():
	symbTrfolder = './'
	symbTrTxtfolder = os.path.join(symbTrfolder, 'txt/')
	symbTrPdffolder = os.path.join(symbTrfolder, 'SymbTr-pdf/')
	symbTrMu2folder = os.path.join(symbTrfolder, 'mu2/')
	symbTrXmlfolder = os.path.join(symbTrfolder, 'MusicXML/')
	symbTrMidfolder = os.path.join(symbTrfolder, 'midi/')

	symbTr_work_file = os.path.join(symbTrfolder, 'symbTr_mbid.json')

	symbtrtxtnames = get_filenames_in_dir(symbTrTxtfolder, keyword = '*.txt')[2]
	symbtrtxtnames = [s for s in symbtrtxtnames if not s[0] == '.']
	symbtrtxtnames = set([os.path.splitext(s)[0] for s in symbtrtxtnames])
	
	symbtrmu2names = get_filenames_in_dir(symbTrMu2folder, keyword = '*.mu2')[2]
	symbtrmu2names = [s for s in symbtrmu2names if not s[0] == '.']
	symbtrmu2names = set([os.path.splitext(s)[0] for s in symbtrmu2names])

	symbtrpdfnames = get_filenames_in_dir(symbTrPdffolder, keyword = '*.pdf')[2]
	symbtrpdfnames = [s for s in symbtrpdfnames if not s[0] == '.']
	symbtrpdfnames = set([os.path.splitext(s)[0] for s in symbtrpdfnames])

	symbtrxmlnames = get_filenames_in_dir(symbTrXmlfolder, keyword = '*.xml')[2]
	symbtrxmlnames = [s for s in symbtrxmlnames if not s[0] == '.']
	symbtrxmlnames = set([os.path.splitext(s)[0] for s in symbtrxmlnames])

	symbtrmidnames = get_filenames_in_dir(symbTrMidfolder, keyword = '*.mid')[2]
	symbtrmidnames = [s for s in symbtrmidnames if not s[0] == '.']
	symbtrmidnames = set([os.path.splitext(s)[0] for s in symbtrmidnames])

	symbTr_work = json.load(open(symbTr_work_file, 'r'))
	symbtrjsonnames = set(s['name'] for s in symbTr_work)

	return (symbtrtxtnames, symbtrmu2names, symbtrpdfnames, 
		symbtrxmlnames, symbtrmidnames, symbtrjsonnames)

def setDiff(set1, set2):
	diff = set1 - set2
	if len(diff) > 0:
		for d in diff:
			print "Name mismatch in " + d

	return diff