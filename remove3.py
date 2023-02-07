lst = [1, 3, 3, 3, 33]
def rem3(lst):
	# for i in lst:
	# 	if i==3:
	# 		lst.remove(i)
	
	i = 0
	while i<len(lst):
		if lst[i]==3:
			del lst[i]
		else:
			i += 1
print(rem3(lst))
print(lst)