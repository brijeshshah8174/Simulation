from calulation import frequency_calc
import matplotlib.pyplot as plt
import reader as r
import sys as s

def plot_it(x,size):
    y = x[1:]+[x[-1]]
    plt.scatter(x,y,marker='p')
    plt.show()
    return True


def histogram(x,y,xlabel,ylabel):
    plt.plot(x,y,color='red')
    plt.bar(x,y,width=0.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    return True




if __name__ =='__main__':
    try:
        assert(len(s.argv)>=2)
    except:
        print("Please insert file name")
        print("May be specified is reside in your system")
    x = r.read_csv(s.argv[1])
    plot_it(x,len(x))
    x,y=frequency_calc(x,int(s.argv[2]))
    histogram(x,y,"x_axis","y_axis")
