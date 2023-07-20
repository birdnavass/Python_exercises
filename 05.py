'''Cree un programa que almacene el abecedario en una lista, elimine de la lista las letras que
ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.'''


abecedario1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'] 
abecedario2 = []

print("\nAbecedario completo: \n",abecedario1)

for i in range(len(abecedario1)):
    if i % 3 != 0:
        abecedario2.append(abecedario1[i])

print("\nAbecedario sin multiplos de 3: \n",abecedario2,"\n")