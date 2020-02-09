import csv

def read_csv(filename):
	with open(filename,'r') as fp:
		ls = list(map(lambda x:float(x[0]),csv.reader(fp)))
	return ls

def read_text(filename):
	with open(filename,'r') as fp:
		ls = list(map(lambda x:float(x.strip('\n')),fp.readline())) 
	return ls

def print_tab(res):
	n = len(res["Aj"])
	if type(res["ej"])!=type([]):
		res["ej"] = [res["ej"] for i in range(n)]
	print("{}		{}		{}		{}	".format("Aj","Oj","Ej","(Ej-Oj)**2/Ej"))
	print("-----------------------------------------------------------")		
	for i in range(n):
			print("{}		{}		{}		{}	".format(res["Aj"][i],res["oj"][i],res["ej"][i],res["v"][i]))
	print("-----------------------------------------------------------")
	print("chi square value",res["chi square value"])
