#I.G : @deeplearningindia

############# USING NON-LoCAL TO CHANGE THE SCOPE ################
def hp_outer():
	x = 8

	def hp_inner():
		nonlocal x
		x+=1
		print("Inside HP_INNER :",x)

	hp_inner()
	return x

Ans = hp_outer()
print("Value of x in HP_OUTER :", Ans)

