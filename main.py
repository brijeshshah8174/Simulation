import calulation as c
from sys import version_info
import csv
import reader as r

if __name__=='__main__':
	if version_info[0]>=3:	
		file_name = input("Enter data file name : ")	
	else:
		file_name = raw_input("Enter data file name :")		
	interval = int(input("Enter interval : "))
	#print("File name is :{} and interval is {}".format(file_name,interval))
	try:	
		ls = r.read_csv(file_name)
	except IOError as e:
		print(str(e))
	res = c.uniform_chi_square_test(ls,len(ls),interval)	
	r.print_tab(res)
