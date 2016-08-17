import os
output = open("clearOutput.txt",'w')
def checkfeed():
	temp = [f+"\n" for f in os.listdir('.') if os.path.isfile(f)]
	try:
		temp.index("feed.txt\n")
	except ValueError:
		print("Creating feed.txt")
		file = open("feed.txt","w")
		file.writelines(temp)
def shrinkFiles():
	checkfeed()
	files = [file.strip() for file in open('feed.txt','r').readlines()]	
	for file in files:
		removeEmptyLines(file)
def removeEmptyLines(fileName):
	file = open(fileName,'r')
	lines = file.readlines()
	file.close()
	file = open(fileName,'w')
	for l in lines:
		if len(l.strip())>0:
			file.write(l)
	file.close()		

def removeComments(fileName):
	def isComment(line):
		comments=["*","//","// ","*/","* ","/*","/**","#"," #"]
		ending=[" */","*/","**/","#"," #"]
		for i in comments:
			if line.startswith(i):
				return True 
		for i in ending:
			if line.endswith(i):
				return True 	
		return False				
	lines = open(fileName,'r').readlines()
	for line in lines:
		if not isComment(line.strip()) and len(line.strip())>0:
			output.write(line)
removeComments("sample.txt")