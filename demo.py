import pyscripts
def showMenu(file):
	print("Select 1 to remove empty lines 2 to remove comments 3 to do all of these things:\n")
	sel = int(input())
	if sel == 3:
		pyscripts.remove_comments(filename)
		pyscripts.remove_empty_lines(filename)
	elif sel == 2:			
		pyscripts.remove_comments(filename)
	elif sel == 1:
		pyscripts.remove_empty_lines(filename)	
	else:
		return
filename = input("Give me a file name(with absolute or relative path):")
while True:
	showMenu(filename)
