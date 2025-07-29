# defining the prime check function

def prime_chk(num):

    if num <= 1:

        return False

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:

            return False

        return True 

ans = int(input("Enter a number to check for prime: "))

print(f"The number {ans} is prime: {prime_chk(ans)}")
