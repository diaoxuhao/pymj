#由下往上
def readyi(infile):
	flag = 0
	jishu = 0
	mydic = {}
	for line in infile:
		line = line.strip()
		if line.strip() =='':
			flag = 1
		elif flag == 1:
			mykey = line.strip()
			mynumber = []
			flag = 2
		elif flag ==2 and ("初六"in line or "初九"in line):
			if "初九" in line:
				mynumber.append(1)
			elif "初六"in line:
				mynumber.append(0)
			flag = 3
		elif flag == 3:
			if "九二" in line:
				mynumber.append(1)
			elif "六二"in line:
				mynumber.append(0)
			flag = 4
		elif flag == 4:
			if "九三" in line:
				mynumber.append(1)
			elif "六三"in line:
				mynumber.append(0)
			flag = 5
		elif flag == 5:
			if "九四" in line:
				mynumber.append(1)
			elif "六四"in line:
				mynumber.append(0)
			flag = 6
		elif flag == 6:
			if "九五" in line:
				mynumber.append(1)
			elif "六五"in line:
				mynumber.append(0)
			flag = 7
		elif flag == 7:
			if "上九" in line:
				mynumber.append(1)
			elif "上六"in line:
				mynumber.append(0)
			flag = 0
#			mynumber = mynumber.reverse()
			mystr = str(mynumber)
			mydic[mystr] = mykey
	return mydic


