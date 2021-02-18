def fib_n_iterative(n):
    fib = [0,1]
    if(n == 0):
        return fib[0]
    for i in range(2,n+1):
        element = fib[i-1] + fib[i-2]
        fib.append(element)
    return fib[n]

#Recursiva sin programacion dinamica
def fib_n_recursive(n):
   if (n == 0):
      return 0
   if (n == 1):
      return 1
   return fib_n_recursive(n-1) + fib_n_recursive(n-2)

def fib_dp(n, cache = {0 : 0, 1 : 1}):
   if n in cache:
      return cache[n]
   cache[n] = fib_dp(n-1, cache) + fib_dp(n-2, cache)
   return cache[n]

