from modules import sheetoperator

def test():
	print(sheetoperator.eqfteams[0])	

def exec():
	lines = []
	with open(r"modules/indextemplate.html", 'r') as fp:
		lines = fp.readlines() 

	with open(r"templates/index.html", 'w') as fp:
		for number, line in enumerate(lines):
			if number not in [38, 53, 68, 83, 98, 113]: #Lines that the code will delete
				fp.write(line)


	#Adding the names
	with open("templates/index.html", "r") as readingfile:
		rcontents = readingfile.readlines()		

	rcontents.insert(38, sheetoperator.eqfteams[0])
	rcontents.insert(53, sheetoperator.eqnfteams[0])
	rcontents.insert(68, sheetoperator.indnfnames[0])
	rcontents.insert(83, sheetoperator.indfnames[0])
	rcontents.insert(98, sheetoperator.indpetnames[0])
	rcontents.insert(113, sheetoperator.indgrnames[0])
	

	with open("templates/index.html", "w") as f:
		rcontents = "".join(rcontents)
		f.write(rcontents)