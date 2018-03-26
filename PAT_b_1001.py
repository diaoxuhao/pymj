
n = int(input());
flag = 0
while True:
	if n == 1:
		print(flag)
		break
	elif n%2==0:
		n /= 2
		flag += 1
	else:
		n = (3*n+1)/2
		flag += 1
