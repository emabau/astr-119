import numpy as np 

def main(): 
	i = 0				# define i as 0
	n = 10 				# define n as 10
	x = 119.0			# use "." to declare floating point number 

	y = np.zeros(n,dtype=float) #declares 10 zeroes as floats

	for i in range(n):		#i in range [0,n-1]
		y[i] = 2.0 * float(i) + 1. #set y=2i+1 as floats 

	for y_element in y: 	# iterate through a variable
		print(y_element)

#execute main function 
if __name__ == "__main__":
	main()