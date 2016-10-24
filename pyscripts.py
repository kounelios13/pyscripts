def isLineEmpty(line):
	return len(line.strip())< 1
def isComment(line,isPythonFile = False):
	comments=["*","//","// ","*/","* ","/*","/**","#"," #","'''"]
	ending=[" */","*/","**/","#"," #","'''"]
	if isPythonFile == True:
		comments.append("#"," #","'''")
		ending.append("#"," #","'''")
	for i in comments:
		if line.startswith(i):
			return True 
	for i in ending:
		if line.endswith(i):
			return True 	
	return False
def getFileExtension(file): 
	return file.split(".")[1]	
def fileExists(file):
	try:
		f=open(file,'r')
		f.close()
	except FileNotFoundError:
		return False
	return True	
def removeEmptyLines(file):
	lines = []
	if not fileExists(file):
		print ("{} does not exist ".format(file))
		return
	out = open(file,'r+')
	lines = out.readlines()
	out.seek(0)
	out.writelines([line for line in lines  if not isLineEmpty(line)])	
	out.close()
def removeComments(file):
	if not fileExists(file):
		raise FileNotFoundException("Requested file was not found")
	pythonExtensions = ["py","py3","pxd","pyx"];
	isPython = True
	try:
		pythonExtensions.index(getFileExtension(file))
	except ValueError:
		isPython = False
	f = open(file,'r+')
	lines = f.readlines()	
	f.writelines([l for l in lines if not isComment(l,isPython)])