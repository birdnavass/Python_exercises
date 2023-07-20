'''Realice un programa que almacene en una lista los números de la serie Fibonacci (0, 1, 1, 2, 3, 5,
8, etc.) generados hasta un numero introducido por el usuario. Por ejemplo, si un usuario ingresa
10, la serie solo mostrara los valores 0, 1, 1, 2, 3, 5 y 8'''


fib = [0,1]

n = int(input("\nIngrese el numero limite: "))

i=1
while fib[i] <= n:
    
    c = i - 1
    fib.append(int(fib[c])+int(fib[i]))
    i += 1

fib.pop()
print("\n",fib,"\n")
