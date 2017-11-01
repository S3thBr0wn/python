from random import randint
def randlist(r,alpha,usedlist,done):
	c = alpha[r]
	print (c)
	usedlist[r] = 1
	sum = 0
	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
		if sum == 5:
				done = True
	return c,usedlist,done
		
def main():
	###############
	alpha = []
	used = []
	for i in range(33,127):
		lttr = chr(i)
		#print(i," ",lttr,end=" ")
		alpha.append(lttr)
		used.append(0)
	print (alpha)
	
	###############
	
	done = False
	while done == False:
		r = randint(0,4)
		print ("r = ",r)
		if used[r] == 0:
			c,used,done = randlist(r,alpha,used,done)
			print (r,c,used,done)
			#print(c,end='')
main()
