# 0 1 2 3 4 5 6 ...
# 0 1 1 2 3 5 8 ...


def recursion_fib(n):
    if n == 1 or n == 2:
        result = 1
        return result
    else:
        result = recursion_fib(n - 1) + recursion_fib(n - 2) # T(n) = O(2^n)
        return result


def memoization_fib(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n==1 or n==2:
        result = 1
    else:
        result = memoization_fib(n-1, memo) + memoization_fib(n-2, memo) #T(n) = O(2^n)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None]*(n+1)
    return memoization_fib(n,memo)



def tabuletion_fib(n):
    if n==1 or n==2:
        result = 1
        return result
    tabul = [None]*(n+1)
    tabul[1]=1
    tabul[2]=1
    for i in range(3, n+1):
        tabul[i] = tabul[i-1] + tabul[i-2] #T(n) = O(n)
    return tabul[n]


#value check.......   5  20 35 ...

try:
    print(fib_memo(999))

except:
    print("cant calculate more than 998")

# print(1 / 0)
print(tabuletion_fib(998))

print(recursion_fib(35))

