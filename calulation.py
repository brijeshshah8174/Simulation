

from math import sqrt,exp


def maxc(ls):
	max1=ls[0]
	for i in ls[1:]:
		if(max1<i):
			max1=i
	return max1


def minc(ls):
	min1=ls[0]
	for i in ls[1:]:
		if(min1>i):
			min1=i
	return min1


def sum_of(ls):
	sum1=0.0
	for i in ls:
		sum1=sum1+i
	return sum1


def mean1(ls):
	total=sum_of(ls)
	mean_of=total/float(len(ls))
	return mean_of


def variance(ls):
	mean = mean1(ls)
	return sum_of(list(map(lambda x:(x-mean)**2,ls)))/(len(ls))

def std(ls):
	return sqrt(variance(ls))

def frequency_calc(ls,interval):
	min1,max1 = minc(ls),maxc(ls)
	step = (max1-min1)/(interval)
	prev = min1
	x_label = []
	y_label = []
	min1+=step
	while(min1<=max1):
		x_label.append(min1)
		min1+=step
	if(x_label[-1]==max1):
		x_label.append(12323435345)
	for i in x_label:
		count = 0
		for j in ls:
			if(j>=prev and j<i):
				count+=1
		prev = i		
		y_label.append(count)
	return x_label,y_label



def unifrom_paramerter_estimate(ls):
	mean,var =mean1(ls),variance(ls)	
	b = (2*mean+sqrt(12*var))/2
	a = 2*mean-b
	print(b,a)
	return b,a

def uniform_chi_square_test(ls,size,interval):
    aj,oj =frequency_calc(ls,interval)
    (b,a) = unifrom_paramerter_estimate(ls)
    ej = float(size/interval)
    v = []
    for i in oj:
        v.append((ej-i)**2/ej)
    return {"Aj":aj,"oj":oj,"ej":ej,"v":v,"chi square value":sum_of(v)}




def exponential_parameter_estimation(ls):
	lamda = 1/mean_of(ls)
	return lamda

def exponential_chi_square_test(ls,interval):
	aj,oj = frequency_calc(ls,interval)
	lamda = exponential_parameter_estimation(ls)
	min1 = minc(ls)	
	ej = []
	v = []
	for i in aj:
		ej.append(exp(-lamda*min1)-exp(-lamda*i)) #
		min1 = i
	for i in zip(ej,oj):
		v.append((i[0]-i[1])**2/i[0])
	return {"Aj":aj,"oj":oj,"ej":ej,"v":v,"chi square value":sum_of(v)}



