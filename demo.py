from pyscripts import Pyscripts as pyscripts
def showMenu(file):
	sel = int(input("Select 1 to remove empty lines 2 to remove comments 3 to do all of these things:\n"))
	if sel == 3:
		pyscripts.remove_comments(filename)
		pyscripts.remove_empty_lines(filename)
		print("Removed comments and blank lines\n")
	elif sel == 2:			
		pyscripts.remove_comments(filename)
		print("Removed comments\n")
	elif sel == 1:
		pyscripts.remove_empty_lines(filename)
		print("Removed blank lines\n")	
	else:
		return
filename = input("Give me a file name(with absolute or relative path):")
while True:
	showMenu(filename)
