# star.py

def s(n):
	if n==1:
	    return ['*']
	return s(n/3)*4+[' ']*len(s(n/3))+s(n/3)*4

def f(s, i, n):
	if n == 3:
		return s[i]
	return f(s, i, n//3)+f(s, i+(n//3)*(n//3)//9, n//3)+f(s, i+(n//3)*(n//3)//9*2,n//3)

def g(s, i, m, n):
	if m == 3:
		return f(s,i,n)+f(s,i+n*n//9,n)+f(s,i+n*n//9*2,n)
	return g(s,i, m//3, n)+g(s,i+(m//3)*(m//3)//3, m//3, n)+g(s,i+(m//3)*(m//3)//3*2,m//3, n)

n=int(input())
a=g(s(n),0,n,n)+g(s(n),n*n//3,n,n)+g(s(n),n*n//3*2,n,n)

for i in range(n):
	for j in range(n):
		print(a[n*i+j],end="")
	print("")
