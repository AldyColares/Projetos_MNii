import re
arquivo = open("arquivo1.txt")
m = int(arquivo.readline().rstrip('\n'))
txt = arquivo.read()
print "grau =",m
print "\nxi\tf(xi)"
print txt
dados = map(float, re.split('\t|\n',txt))
arquivo.close()
a = dados[0]
b = dados[m*2]
fx0 = dados[1]
fxm = dados[m*2+1]
h = (b - a)/m
L = range(m+1)
i=1
j=0
S1=0
S2=0
k=1
while ( i <= m*2+1 ):
	L[j] = dados[i]
	i = i+2
	j = j+1
while(k<m):
	if int(k) % 3 == 0:
		S1 = S1 + L[k]	
	else:
		S2 = S2 + L[k]	
	k = k+1
I = (3*h/8)*(fx0 + fxm + 3*S2 + 2*S1)
print "\na =",a
print "b =",b
print "h =",h
print "f(x0) =",fx0
print "f(xm) =",fxm
print "Somatorio de impar =",S2
print "Somatorio de par =",S1
print "\nI =",I
