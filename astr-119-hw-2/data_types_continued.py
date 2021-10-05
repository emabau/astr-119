#string 
s = "I am a string."
print(type(s))		#will say str 

#boolean 

yes = True 			#Boolean True 
print(type(yes))

no = False 			#Boolean false 
print(type(no))

#list -- ordered and changeable 

alpha_tuple = ["a","b","c"]	#list initialization 
print(type(alpha_tuple))	#will say tuple

try:
	alpha_tuple[2]="d"		#will rise TypeError
except TypeError:
	print("We can't add elements to tuples!")	#prints message 
print(alpha_tuple) 	#print tuple 
