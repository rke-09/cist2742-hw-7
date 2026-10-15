# Question 5 

def gcd(m, n):
    while n != 0:
        m, n = n, m % n

    return m

def phi(n):
    numbers = []

    for i in range(1, n):
        if gcd(n, i) == 1:
            numbers.append(i)

    return numbers

def main():
    n = int(input("Enter a positive integer: "))

    result = phi(n)

    print("Relatively prime numbers:", result)
    print("Euler's totient:", len(result))

main()