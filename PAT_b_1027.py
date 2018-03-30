
instr = input().split(" ")
n = int(instr[0])
mynum = []
sheng = 0
for i in range(1,1001):
	if i==1:
		n -= i
	else:
		n -= 2*(2*i-1)
	if n < 0:
		sheng = n+2*(2*i-1)
		break;
	mynum.append(2*i-1)
mynum.reverse()
flag = 0
for i in mynum:
	print(" "*flag+instr[1]*i)
	flag += 1
mynum.reverse()
flag -=2
for i in mynum:
	if i!=1:
		print(" "*flag+instr[1]*i)
		flag -= 1
print(sheng)
