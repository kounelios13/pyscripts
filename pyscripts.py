import os
def is_line_empty(line):
	return len(line.strip()) < 1
def is_comment(line,isPythonFile = False):
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
def get_file_extension(file): 
	return file.split(".")[1]	
def remove_empty_lines(file):
	lines = []
	with open(file,'r') as in_file:
		lines = in_file.readlines()
	with open(file,'w') as out:
		out.writelines([line for line in lines if not is_line_empty(line)])
def remove_comments(file):
	pythonExtensions = ["py","py3","pxd","pyx"];
	isPython = True
	try:
		pythonExtensions.index(get_file_extension(file))
	except ValueError:
		isPython = False
	with open(file,'r') as in_file:
		lines  = in_file.readlines()
	with open(file,'w') as out:	
		out.writelines([l for l in lines if not is_comment(l,isPython)])
