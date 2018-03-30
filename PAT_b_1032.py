#N = int(input())
#result = {}
#for i in range(N):
#	num,score = tuple(map(int,input().split(" ")))
#	if num in result.keys():
#		result[num] += score
#	else:
#		result[num] = score
#M = max(result.items(),key = lambda x:x[1])
#print(M[0],M[1])

N = int(input())
result = [0]*N
for i in range(N):
	num,score = tuple(map(int,input().split(" ")))
	result[num-1] += score
Max = 0
indx = 0
for i in range(N):
	if result[i] >= Max:
		Max = result[i]
		indx = i
print(indx+1,Max)


