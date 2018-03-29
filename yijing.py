import math
import random
import readyi
infile = open("yi.txt",'r')
mydic = readyi.readyi(infile)
#print(mydic['[0, 1, 0, 0, 0, 1]'])
#由下往上算
s = input("请告诉我想要算的事情:\n")
R = []
for k in range(6):
	#### 一变
	# 一共 49 颗棋子
	sum1 = 49
	# 分为两组：左天右地
	tian = random.randint(5,sum1-5)
	di = sum1 - tian
	# 从地拿走一颗棋子，叫作“人”
	di -= 1
	# 天除以4，计算并减去余数
	yu_tian = tian%4
	if yu_tian == 0:
		yu_tian = 4
	tian -= yu_tian
	# 地除以4，计算并减去余数
	yu_di = di%4
	if yu_di == 0:
		yu_di = 4
	di -= yu_di
	#print(yu_tian+yu_di+1)
	# 二变
	sum2 = tian+di
	tian = random.randint(5,sum2-5)
	di = sum2 - tian
	# 从地拿走一颗棋子，叫作“人”
	di -= 1
	# 天除以4，计算并减去余数
	yu_tian = tian%4
	if yu_tian == 0:
		yu_tian = 4
	tian -= yu_tian
	# 地除以4，计算并减去余数
	yu_di = di%4
	if yu_di == 0:
		yu_di = 4
	di -= yu_di
	# 三变
	sum3 = tian+di
	tian = random.randint(5,sum3-5)
	di = sum3 - tian
	# 从地拿走一颗棋子，叫作“人”
	di -= 1
	# 天除以4，计算并减去余数
	yu_tian = tian%4
	if yu_tian == 0:
		yu_tian = 4
	tian -= yu_tian
	# 地除以4，计算并减去余数
	yu_di = di%4
	if yu_di == 0:
		yu_di = 4
	di -= yu_di
	result = int((tian+di)/4)
	R.append(result)
Result_1 = [y%2 for y in R]
print("**"+mydic[str(Result_1)]+"**")
R1 = R.copy()
R.reverse()
bian = []
for i in range(len(R)):
	if R[i] == 6:
		print("--  --","老阴*变")
		R1[5-i] = 7
		bian.append(5-i)
	elif R[i] == 8:
		print("--  --","少阴")
	elif R[i] == 9:
		print("------","老阳*变")
		R1[5-i] = 6
		bian.append(5-i)
	elif R[i] == 7:
		print("------","少阳")
Result_2 = [y%2 for y in R1]
if Result_2 != Result_1:
	print("**之**")
	print("**"+mydic[str(Result_2)]+"**")
	R1.reverse()
	for i in range(len(R1)):
		if R1[i] == 6:
			print("--  --")
		elif R1[i] == 8:
			print("--  --")
		elif R1[i] == 9:
			print("------")
		elif R1[i] == 7:
			print("------")
infile.close()
infile = open("yi.txt",'r')
print("结果：")
if len(bian) == 1 or len(bian)==2:
	mubiao = -2
	flag = mubiao
	print(mydic[str(Result_1)]+"卦之爻辞")
	for line in infile:
		line = line.strip()
		if line == mydic[str(Result_1)]:
			flag = mubiao+1
		elif flag != mubiao and flag < bian[0]:
			flag += 1
		elif flag == bian[0]:
			print(line)
			flag = mubiao
if len(bian)==3 or len(bian)==0:
	mubiao = -2
	flag = mubiao
	print(mydic[str(Result_1)]+"卦之爻辞")
	for line in infile:
		line = line.strip()
		if line == mydic[str(Result_1)]:
			flag = mubiao+1
		elif flag != mubiao and flag < -1:
			flag += 1
		elif flag == -1:
			print(line)
			flag = mubiao
if len(bian) == 4:
	mubiao = -2
	flag = mubiao
	print(mydic[str(Result_2)]+"卦之爻辞")
	for line in infile:
		line = line.strip()
		if line == mydic[str(Result_2)]:
			flag = mubiao+1
		elif flag != mubiao and flag < bian[0]:
			flag += 1
		elif flag == bian[0]:
			print(line)
			flag = mubiao
