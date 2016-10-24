import pyscripts
def showMenu():
	filename = input("Give me a file name(with absolute or relative path):")
	print("Select 1 to remove empty lines 2 to remove comments 3 to do all of these things:\n")
	sel = int(input())
	if sel == 3:
		pyscripts.removeComments(filename)
		pyscripts.removeEmptyLines(filename)
	elif sel == 2:			
		pyscripts.removeComments(filename)
	elif sel == 1:
		pyscripts.removeEmptyLines(filename)	
	else:
		return
while True:
	showMenu()

