#Algumas sintaxes para manipular arquivo.

arq =open("arquivo.txt","r")

texto_todo = arq.read()
print "\n",texto_todo

arq.close()

arq =open("arquivo.txt","r")

#variavel texto e uma lista de string onde cada linha do arquivo e um indice da lista. 
texto = arq.readlines()

#Tamanho da lista
tamanho_lista=len(texto)

#particiona uma string, onde cada particao termina em cada espaco da string. O indice [2] e para armazenar a segunda particao da string
x = texto[2].split()[2]

print "\n", texto ,"\n",tamanho_lista, "\n", x 

arq.close()



