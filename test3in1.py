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
S=0
i=1
while ( i <= m*2+1 ):
	S = S + dados[i]
	i = i+2
I1 = (h/2)*(fx0 + fxm) + h*(S-(fx0 + fxm))
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
	if int(k) % 2 == 0:
		S1 = S1 + L[k]	
	else:
		S2 = S2 + L[k]	
	k = k+1
I2 = (h/3)*(fx0 + fxm + 4*S2 + 2*S1)
S1=0
S2=0
k=1
while(k<m):
	if int(k) % 3 == 0:
		S1 = S1 + L[k]	
	else:
		S2 = S2 + L[k]	
	k = k+1
I3 = (3*h/8)*(fx0 + fxm + 3*S2 + 2*S1)
print "\nI Trap =",I1
print "\nI 1/3 Simp =",I2
print "\nI 3/8 Simp =",I3
