N = int(input())
result = {}
for i in range(N):
	num,score = tuple(map(int,input().split(" ")))
	if num in result.keys():
		result[num] += score
	else:
		result[num] = score
M = max(result.items(),key = lambda x:x[1])
print(M[0],M[1])
