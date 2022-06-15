from modules import sheetoperator, nonetodash
from functools import reduce
import time

def exec():
	header = ''
	podium = []


	# HEADER CONTROL
	with open(r"modules/templates/eqf/headertemplate.html", 'r') as fp:
		header = fp.read() 

	with open('templates/eqf.html', 'w') as f:
		f.write(header)

	# HEADER CONTROL


	# PODIUM CONTROL
	with open(r"modules/templates/eqf/podiumtemplate.html", 'r') as fp:
		podium = fp.readlines()

	with open(r"test.html", 'w') as fp:
		for number, line in enumerate(podium):
			if number not in [1, 4, 6, 9, 12, 17, 38, 41, 44, 47, 50, 53]: #Lines that the code will delete
				fp.write(line)

	# Step 1: read the document by lines
	with open("test.html", "r") as readingfile:
		rcontents = readingfile.readlines()

	# Step 3: Edit the podium with a loop
	i = 0
	while i <=4:	
		rcontents.insert(1, str(f'"{i+1}"'))
		rcontents.insert(4, '<img class="badge podiumelement" src="../static/badges/badge1.png">')
		rcontents.insert(7, str(nonetodash.nonetodash(sheetoperator.eqfteams[int(i)])))
		rcontents.insert(10, str(nonetodash.nonetodash(sheetoperator.eqftotpunts[int(i)])))
		rcontents.insert(15, f'"t{i+1}"')
		rcontents.insert(36, str(nonetodash.nonetodash(sheetoperator.eqfdilluns[int(i)])))
		rcontents.insert(39, str(nonetodash.nonetodash(sheetoperator.eqfdimarts[int(i)])))
		rcontents.insert(42, str(nonetodash.nonetodash(sheetoperator.eqfdimecres[int(i)])))
		rcontents.insert(45, str(nonetodash.nonetodash(sheetoperator.eqfdijous[int(i)])))
		rcontents.insert(48, str(nonetodash.nonetodash(sheetoperator.eqfdivendres[int(i)])))
		rcontents.insert(51, str(nonetodash.nonetodash(sheetoperator.eqfbitlles[int(i)])))
		i += 1

	# Final step: save and to the list we go
	
	with open("templates/eqf.html", "a") as f:
		rcontents = "".join(rcontents)
		f.write(rcontents)