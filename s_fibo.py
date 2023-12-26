def fibo(n):
    s = [0, 1]
    if n <= 1:
        return s[n]
    
    for i in range(2, n + 1):
        n_fibo = s[i - 1] + s[i - 2]
        s.append(n_fibo)
    
    return s[n]

def fibo_r(n):
    if n <= 1:
        return n
    else:
        return fibo_r(n - 1) + fibo_r(n - 2)

num = int(input("Enter the number: "))
print(fibo(num))
print(fibo_r(num))