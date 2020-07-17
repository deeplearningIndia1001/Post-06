#I.G : @deeplearningindia

############# USING GLOBAL TO CHANGE THE SCOPE ################

x = 8

def hp():
	global x
	x+=1
	print("Inside the function:",x)
	return x

Ans = hp()
print("Outside the FUnction :",Ans)