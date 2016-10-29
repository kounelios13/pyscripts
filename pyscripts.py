import os
def is_line_empty(line):
	return not line.strip()
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
class pyscripts():
	"""A class 	of static methods that help you do things with files"""
	def __init__(self, arg):
		self.arg = arg
	@staticmethod	
	def remove_comments(file):	
		pythonExtensions = ["py","py3","pxd","pyx"];
		isPython = True
		try:
			pythonExtensions.index(file.split(".")[1])
		except ValueError:
			isPython = False
		with open(file,'r') as in_file:
			lines  = in_file.readlines()
		with open(file,'w') as out:	
			out.writelines([l for l in lines if not is_comment(l,isPython)])
	@staticmethod
	def remove_empty_lines(file):
		with open(file,'r') as file_in:
			lines = file_in.readlines()	
		with open(file,'w') as file_out:
			file_out.writelines([l for l in lines if l.strip()])
	# @staticmethod
	# def get_file_extension(file):
	# 	return file.split(".")[1]				
