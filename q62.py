str=input()
x1=[]
for y in str:
	if y not in x1:
		x1.append(y)
	else:
		break
print(len(x1))
