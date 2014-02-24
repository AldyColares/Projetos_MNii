
#inacabado. Falta escrever a entrada do arquivo e a manipular os valores.

h=(b-a)/n #a é o inicio da função e b o final em relação a x da função. 

acumulador 0,0000
primeiro_posicao = f(x0)#f() É a função. 
ultimo_posicao = f(xm)
while a+h < b
  acumulador = acumulador + f(a+h)
  a = a+h

valor_aproximado = primeira_posicao + 2*(acumulador) + ultimo_posicao
print "valor aproximado = ", valor_aproximado 
