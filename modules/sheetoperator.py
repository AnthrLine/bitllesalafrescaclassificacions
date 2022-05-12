from openpyxl import Workbook, load_workbook


indnfnames = []
indnfmitjana = []
indnfbitlles = []
indnfpunts = []
indnftirades = []

indfnames = []
indfmitjana = []
indfbitlles = []
indfpunts = []
indftirades = []

indpetnames = []
indnpetmitjana = []
indpetbitlles = []
indpetpunts = []
indpettirades = []

indgrnames = []
indgrmitjana = []
indgrbitlles = []
indgrpunts = []
indgrtirades = []

eqnfteams = []
eqnfdilluns = []
eqnfdimarts = []
eqnfdimecres = []
eqnfdijous = []
eqnfdivendres = []
eqnftotpunts = []
eqnfbitlles = []

eqfteams = []
eqfdilluns = []
eqfdimarts = []
eqfdimecres = []
eqfdijous = []
eqfdivendres = []
eqftotpunts = []
eqfbitlles = []

def exec():

	#WE LOAD THE WB EVERY TIME SO IT GETS UPDATED WITH THE NEW RESULTS
	workbook = load_workbook(filename="Web.xlsx", data_only=True)
	sheet = workbook.active

	#GET THE NUMBER OF CANDIDATES/TEAMS
	individualsnf = sheet["A1"].value
	individualsf = sheet["B1"].value
	individualspet = sheet["C1"].value
	individualsgr = sheet["D1"].value
	equipsnf = sheet["E1"].value
	equipsf = sheet["F1"].value
	#GET THE NUMBER OF CANDIDATES/TEAMS


	#GET THE NAMES OF THE NF CATEGORY
	
	inf = 1 #Starting pos. is on one to match sheet
	
	while inf <= individualsnf:

		c1 = "B" + str(inf+1)
		c2 = "C" + str(inf+1)
		c3 = "D" + str(inf+1)
		c4 = "E" + str(inf+1)
		c5 = "F" + str(inf+1)
		
		indnfnames.append(sheet[c1].value)
		indnfmitjana.append(sheet[c2].value)
		indnfbitlles.append(sheet[c3].value)
		indnfpunts.append(sheet[c4].value)
		indnftirades.append(sheet[c5].value)
		
		inf = inf + 1

	#GET THE NAMES OF THE NF CATEGORY

	#GET THE NAMES OF THE F CATEGORY
	
	indf = individualsnf + 1 
	
	while indf <= individualsnf+individualsf:
		c1 = "B" + str(indf+1)
		c2 = "C" + str(indf+1)
		c3 = "D" + str(indf+1)
		c4 = "E" + str(indf+1)
		c5 = "F" + str(indf+1)
	
		indfnames.append(sheet[c1].value)
		indfmitjana.append(sheet[c2].value)
		indfbitlles.append(sheet[c3].value)
		indfpunts.append(sheet[c4].value)
		indftirades.append(sheet[c5].value)
	
		indf = indf+1
	#GET THE NAMES OF THE F CATEGORY

	#GET THE NAMES OF THE PET CATEGORY
	
	indpet = individualsnf+individualsf + 1 
	
	while indpet <= individualsnf+individualsf+individualspet:
		c1 = "B" + str(indpet+1)
		c2 = "C" + str(indpet+1)
		c3 = "D" + str(indpet+1)
		c4 = "E" + str(indpet+1)
		c5 = "F" + str(indpet+1)
	
		indpetnames.append(sheet[c1].value)
		indnpetmitjana.append(sheet[c2].value)
		indpetbitlles.append(sheet[c3].value)
		indpetpunts.append(sheet[c4].value)
		indpettirades.append(sheet[c5].value)
	
		indpet = indpet+1
	#GET THE NAMES OF THE PET CATEGORY

	#GET THE NAMES OF THE GR CATEGORY
	
	indgr = individualsnf+individualsf+individualspet + 1 
	
	while indgr <= individualsnf+individualsf+individualspet+individualsgr:
		c1 = "B" + str(indgr+1)
		c2 = "C" + str(indgr+1)
		c3 = "D" + str(indgr+1)
		c4 = "E" + str(indgr+1)
		c5 = "F" + str(indgr+1)
		
	
		indgrnames.append(sheet[c1].value)
		indgrmitjana.append(sheet[c2].value)
		indgrbitlles.append(sheet[c3].value)
		indgrpunts.append(sheet[c4].value)
		indgrtirades.append(sheet[c5].value)
		
		indgr = indgr+1
	#GET THE NAMES OF THE GR CATEGORY

	#GET THE TEAMS INFO ON THE NF CATEGORY

	eqnf = individualsnf+individualsf+individualspet+individualsgr + 1 


	while eqnf <= individualsnf+individualsf+individualspet+individualsgr+equipsnf:
		c1 = "B" + str(eqnf+1)
		c2 = "C" + str(eqnf+1)
		c3 = "D" + str(eqnf+1)
		c4 = "E" + str(eqnf+1)
		c5 = "F" + str(eqnf+1)
		c6 = "G" + str(eqnf+1)
		c7 = "H" + str(eqnf+1)
		c8 = "I" + str(eqnf+1)
	
		eqnfteams.append(sheet[c1].value)
		eqnfdilluns.append(sheet[c2].value)
		eqnfdimarts.append(sheet[c3].value)
		eqnfdimecres.append(sheet[c4].value)
		eqnfdijous.append(sheet[c5].value)
		eqnfdivendres.append(sheet[c6].value)
		eqnftotpunts.append(sheet[c7].value)
		eqnfbitlles.append(sheet[c8].value)
		
		eqnf = eqnf+1
	
	#GET THE TEAMS INFO ON THE NF CATEGORY
	
	#GET THE TEAMS INFO ON THE F CATEGORY

	eqf = individualsnf+individualsf+individualspet+individualsgr+equipsnf + 1 



	while eqf <= individualsnf+individualsf+individualspet+individualsgr+equipsnf+equipsf:
		c1 = "B" + str(eqf+1)
		c2 = "C" + str(eqf+1)
		c3 = "D" + str(eqf+1)
		c4 = "E" + str(eqf+1)
		c5 = "F" + str(eqf+1)
		c6 = "G" + str(eqf+1)
		c7 = "H" + str(eqf+1)
		c8 = "I" + str(eqf+1)
	
		eqfteams.append(sheet[c1].value)
		eqfdilluns.append(sheet[c2].value)
		eqfdimarts.append(sheet[c3].value)
		eqfdimecres.append(sheet[c4].value)
		eqfdijous.append(sheet[c5].value)
		eqfdivendres.append(sheet[c6].value)
		eqftotpunts.append(sheet[c7].value)
		eqfbitlles.append(sheet[c8].value)
		
		eqf = eqf+1
		print(eqfteams)
	#GET THE TEAMS INFO ON THE F CATEGORY
	return("Done")