# Função recursiva
def Fibonacci_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return Fibonacci_rec(n-1) + Fibonacci_rec(n-2)

print(Fibonacci_rec(10))

#função interativa
def Fibonacci_int(n):
    antPenul=0
    penul=1
    if n==0 or n==1:
        return n
    for i in range(2,n+1):
        atual=antPenul + penul
        antPenul=penul
        penul=atual
    return atual

print(Fibonacci_int(10))
        
        