def factorial(n):
    ans = 1
    i = 2
    #calculating the factorial
    while (i <= n):
        ans *= i
        i += 1
    return ans

if __name__ == "__main__":
    num = int(input())
    print(factorial(num))
