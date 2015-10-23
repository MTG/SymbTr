import os
import fnmatch

def getFileNamesInDir(dir_name, keyword = '.mp3', skip_foldername = '', 
					matchCase = True, verbose = False):
	names = []
	folders = []
	fullnames = []

	if verbose:
		print dir_name

	# check if the folder exists
	if not os.path.isdir(dir_name):
		if verbose:
			print "> Directory doesn't exist!"
		return [], [], []

	# if the dir_name finishes with the file separator, 
	# remove it so os.walk works properly
	dir_name = dir_name[:-1] if dir_name[-1] == os.sep else dir_name

	# walk all the subdirectories
	for (path, dirs, files) in os.walk(dir_name):
		for f in files:
			hasKey = (fnmatch.fnmatch(f, keyword) if matchCase else 
				fnmatch.fnmatch(f.lower(), keyword.lower()))
			if hasKey and skip_foldername not in path.split(os.sep)[1:]:
				folders.append(unicode(path, 'utf-8'))
				names.append(unicode(f,'utf-8'))
				fullnames.append(os.path.join(path,f))

	if verbose:
		print "> Found " + str(len(names)) + " files."
	return fullnames, folders, names