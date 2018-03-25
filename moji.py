import math
import random
import functools
#a,b,c = map(int,input("give me 3 numbers\n").split());

def triangle(a,b,c):
#	a=a//3;
	x = (a+b+c)/2;
	s = math.sqrt(x*(x-a)*(x-b)*(x-c));
	if s >=0 :
		print("s>=0");
	elif s<2:
		print(s<0);
	else:
		print("ha?");
	return s;

#p = triangle(a,b,c);
def jiecheng(n):
	if n==1 or n ==0:
		return 1;
	else:
		return n*jiecheng(n-1);
#n = int(input("give me a number"));
#print("the factorial of ",n,"is",jiecheng(n));


def outstream(n,m):
	n = int(input("give me a number:"));
	while n>=10:
		n-=1;
	m =jiecheng(n);
	print("the jiecheng of number",n,"is",m);
	return;
#print("the area of the triangle you have given me is:");
#print(p);

def mysqrt(x):
	assert x>=0;
	if x ==0:
		return 0;
	else:
		z = random.randint(1,10);
		y = x/z;
		flag = 0;
		while  math.fabs(y*y - x)>=1e-6:
			z = (z+y)/2;
			y = x/z;
			flag+=1;
			print(y);
		return y;

def printstr(s):
	for i in s:
		print(i);
	return;

#n = int(input("give me a number"));
#mysqrt(n);
#del(n);

def lifanggen(x):
	x0 = x;
	while True:
		x1 = (2*x0+x/x0**2)/3;
		if math.fabs((x1-x0)/x0)<1e-6:
			break;
		x0 = x1;
	return x1;
#n = int(input("give me a number\n"));
#print(lifanggen(n));

#b = 1;
#def operate_b():
##	global b;
#	b = 3;
#	print(b);
#operate_b();
#print(b);

#a = 1;
#b = 1.1;
#a /=3;
#print(isinstance(a,int),isinstance(b,int))
b = 0
a = 1 if b>0 else 2;
# a = b>0 ? 1:2
def test_chengmi():
	def new_chengmi(x,n):
		assert isinstance(x,int) and isinstance(n,int)
		if n == 1:
			return x;
		elif n==0:
			return 1;
		elif n%2 == 0:
			return new_chengmi(x*x,n//2);
		elif n%2 == 1:
			return x*new_chengmi(x,n-1);
		else:
			pass;
	x,n = map(int,input("give me 2 numbers:").split());
	print(new_chengmi(x,n));

#test_chengmi();

def func1(x):
	return 10 if x==1 else func2(x-1);
def func2(x):
	return 9 if x==1 else func1(x-1);
#print(func1(100));

def test_func(func3,a,*args):
	print(func3(a));
	for i in args:
		print(i);
	print(args[0])
	
#test_func(func1,2,3,4,5,6,7);

def lambda_learn():
	li1 = [1,2,3,4];
	li2 = [6,7,8,9];
	map_li = map(lambda a,b : a+b,li1,li2);
	filter_li = filter(lambda a:a>2, li1);
	reduce_li = functools.reduce(lambda a,b:a+b,li1);
	print(list(map_li));
	print(list(filter_li));
	print(reduce_li);
#lambda_learn();
t = list( map(lambda x : x*x, [y for y in range(0,11)]));

def newton(f):
	def diff(f,x):
		d = 1e-8;
		return (f(x+d)-f(x))/d;
	x0 = 1+10*math.pi;
	while True:
		x = x0 - f(x0) / diff(f,x0);
		if math.fabs(x-x0) < 1e-6:
			return x;
		else:
			x0 = x;


#y = newton(math.sin);
#print(y);

def Monte_Carlo(n):
	def isprime(a,b):
		for i in range(2,min(b,a)+1):
			if a%i == 0 and b%i == 0:
				return True;
		return False;
	m = 0;
	for i in range(n):
		a = random.uniform(-1.0,1.0);
		b = random.uniform(-1.0,1.0);
		if math.hypot(a,b)<=1.0:
			m+=1;
	return 4*m/n
#print(Monte_Carlo(1000000));
#print("diaoxuhao","dashazi",sep=",",end="  %%\n");
#
#ppp = "diao"+"xuhao";
#print(len(ppp));
#a=" `";
#print(a)

def str_learn():
	a = "dIaOxUhAo";
	b = list(a);
	c = "".join(b);
	print(c);
	return;

def mylist():
	a = [ y for y in range(0,100)]
	b = list(range(0,100))
	c = range(0,100)
	for i in range(0,len(b)):
		b.append(i-99);
	d = list(filter(lambda a:a >=10 and a<= 15,b))
	x = list("diaoxuhao");
	print(x);
	e = functools.reduce(lambda a,b:a+b,x)
	print(e);

a = [];
a.append(1);
a.append("ha");
print(a);

