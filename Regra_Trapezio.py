arquivo = open("arquivo.txt", "r")

listaStr = arquivo.readlines()

arquivo.close()
#com tres linhas obtenho uma lista de string com toda a tabela nela. 
tamanhoLista = len(listaStr)
tamanhoLista = int(tamanhoLista) 

m = listaStr[0].split()[0]
m = int(m)
a = listaStr[2].split()[1]
a = float(a)
b = listaStr[tamanhoLista-1].split()[1]
b = float(b)

h=(b-a)/m #'a' e o inicio da funcao e 'b' o final em relacao a x da funcao. 
 
funcao_x0 = listaStr[2].split()[2]
funcao_x0 = float(funcao_x0) 
funcao_xm = listaStr[tamanhoLista-1].split()[2]
funcao_xm = float(funcao_xm)

acumulador=0.00000000
while (a+h < b):
  i=4 #depende da posicao da tabela onde esta o f(x) do segundo ponto.
  acumulador = acumulador + float(listaStr[i].split()[2]) 
  a = a+h
  i = i+1  

valor_aproximado = (h/2)*(funcao_x0 + 2*(acumulador) + funcao_xm)
print "valor aproximado = ", valor_aproximado 
