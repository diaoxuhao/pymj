
s = input()
t = list(map(int,(list(s))))
Sum = str(sum(t))
mydic = {'1':'yi','2':'er','3':'san',
			'4':'si','5':'wu','6':'liu',
			'7':'qi','8':'ba','9':'jiu','0':'ling'}
result = []
for k in Sum:
	result.append(mydic[k])
print(" ".join(result))
