def pi(maxK=70, prec=1008, disp=1007):
    from decimal import Decimal as Dec, getcontext as gc
    gc().prec = prec
    K, M, L, X, S = 6, 1, 13591409, 1, 13591409
    for k in range(1, maxK + 1):
        M = Dec((K ** 3 - (K << 4)) * M / k ** 3)
        L += 545140134
        X *= -262537412640768000
        S += Dec(M * L) / X
        K += 12
    pi = 426880 * Dec(10005).sqrt() / S
    pi = Dec(str(pi)[:disp])
    return pi


def isPrime(number):
    assert isinstance(number, int) and (number >= 0), \
        "'number' must been an int and positive"
    if number <= 3:
        return number > 1
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def sieveEr(N):
    from math import sqrt
    assert isinstance(N, int) and (N > 2), "'N' must been an int and > 2"
    primes = [True for x in range(N + 1)]
    for p in range(2, int(sqrt(N)) + 1):
        if (primes[p]):
            for i in range(p*p, N + 1, p):
                primes[i] = False
    primes[0] = False
    primes[1] = False
    ret = []
    for p in range(N + 1):
        if primes[p]:
            ret.append(p)
    return ret


def getPrimeNumbers(N):
    assert isinstance(N, int) and (N > 2), "'N' must been an int and > 2"
    ans = []
    for number in range(2, N + 1):
        if isPrime(number):
            ans.append(number)
    assert isinstance(ans, list), "'ans' must been from type list"
    return ans


def primeFactorization(number):
    assert isinstance(number, int) and number >= 0, \
        "'number' must been an int and >= 0"
    ans = []
    factor = 2
    quotient = number
    if number == 0 or number == 1:
        ans.append(number)
    elif not isPrime(number):
        while (quotient != 1):
            if isPrime(factor) and (quotient % factor == 0):
                ans.append(factor)
                quotient /= factor
            else:
                factor += 1
    else:
        ans.append(number)
    assert isinstance(ans, list), "'ans' must been from type list"
    return ans


def greatestPrimeFactor(number):
    assert isinstance(number, int) and (number >= 0), \
        "'number' bust been an int and >= 0"
    ans = 0
    primeFactors = primeFactorization(number)
    ans = max(primeFactors)
    assert isinstance(ans, int), "'ans' must been from type int"
    return ans


def smallestPrimeFactor(number):
    assert isinstance(number, int) and (number >= 0), \
        "'number' bust been an int and >= 0"
    ans = 0
    primeFactors = primeFactorization(number)
    ans = min(primeFactors)
    assert isinstance(ans, int), "'ans' must been from type int"
    return ans


def isEven(number):
    assert isinstance(number, int), "'number' must been an int"
    assert isinstance(number %
                      2 == 0, bool), "compare bust been from type bool"
    return number % 2 == 0


def isOdd(number):
    assert isinstance(number, int), "'number' must been an int"
    assert isinstance(number %
                      2 != 0, bool), "compare bust been from type bool"
    return number % 2 != 0


def goldbach(number):
    assert isinstance(number, int) and (number > 2) and isEven(number), \
        "'number' must been an int, even and > 2"
    ans = []
    primeNumbers = getPrimeNumbers(number)
    lenPN = len(primeNumbers)
    i = 0
    j = 1
    loop = True
    while (i < lenPN and loop):
        j = i + 1
        while (j < lenPN and loop):
            if primeNumbers[i] + primeNumbers[j] == number:
                loop = False
                ans.append(primeNumbers[i])
                ans.append(primeNumbers[j])
            j += 1
        i += 1
    assert isinstance(ans, list) and (len(ans) == 2) and \
        (ans[0] + ans[1] == number) and isPrime(ans[0]) and isPrime(ans[1]), \
        "'ans' must contains two primes. And sum of elements must been eq 'number'"
    return ans


def gcd(number1, number2):
    assert isinstance(number1, int) and isinstance(number2, int) \
        and (number1 >= 0) and (number2 >= 0), \
        "'number1' and 'number2' must been positive integer."
    rest = 0
    while number2 != 0:
        rest = number1 % number2
        number1 = number2
        number2 = rest
    assert isinstance(number1, int) and (number1 >= 0), \
        "'number' must been from type int and positive"
    return number1


def kgV(number1, number2):
    assert isinstance(number1, int) and isinstance(number2, int) \
        and (number1 >= 1) and (number2 >= 1), \
        "'number1' and 'number2' must been positive integer."
    ans = 1
    if number1 > 1 and number2 > 1:
        primeFac1 = primeFactorization(number1)
        primeFac2 = primeFactorization(number2)
    elif number1 == 1 or number2 == 1:
        primeFac1 = []
        primeFac2 = []
        ans = max(number1, number2)
    count1 = 0
    count2 = 0
    done = []
    for n in primeFac1:
        if n not in done:
            if n in primeFac2:
                count1 = primeFac1.count(n)
                count2 = primeFac2.count(n)
                for i in range(max(count1, count2)):
                    ans *= n
            else:
                count1 = primeFac1.count(n)
                for i in range(count1):
                    ans *= n
            done.append(n)
    for n in primeFac2:
        if n not in done:
            count2 = primeFac2.count(n)
            for i in range(count2):
                ans *= n
            done.append(n)
    assert isinstance(ans, int) and (ans >= 0), \
        "'ans' must been from type int and positive"
    return ans


def getPrime(n):
    assert isinstance(n, int) and (n >= 0), "'number' must been a positive int"
    index = 0
    ans = 2
    while index < n:
        index += 1
        ans += 1
        while not isPrime(ans):
            ans += 1
    assert isinstance(ans, int) and isPrime(ans), \
        "'ans' must been a prime number and from type int"
    return ans


def getPrimesBetween(pNumber1, pNumber2):
    assert isPrime(pNumber1) and isPrime(pNumber2) and (pNumber1 < pNumber2), \
        "The arguments must been prime numbers and 'pNumber1' < 'pNumber2'"
    number = pNumber1 + 1
    ans = []
    while not isPrime(number):
        number += 1
    while number < pNumber2:
        ans.append(number)
        number += 1
        while not isPrime(number):
            number += 1
    assert isinstance(ans, list) and ans[0] != pNumber1 \
        and ans[len(ans) - 1] != pNumber2, \
        "'ans' must been a list without the arguments"
    return ans


def getDivisors(n):
    assert isinstance(n, int) and (n >= 1), "'n' must been int and >= 1"
    ans = []
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            ans.append(divisor)
    assert ans[0] == 1 and ans[len(ans) - 1] == n, \
        "Error in function getDivisiors(...)"
    return ans


def isPerfectNumber(number):
    assert isinstance(number, int) and (number > 1), \
        "'number' must been an int and >= 1"
    divisors = getDivisors(number)
    assert isinstance(divisors, list) and (divisors[0] == 1) and \
        (divisors[len(divisors) - 1] == number), \
        "Error in help-function getDivisiors(...)"
    return sum(divisors[:-1]) == number


def simplifyFraction(numerator, denominator):
    assert isinstance(numerator, int) and isinstance(denominator, int) \
        and (denominator != 0), \
        "The arguments must been from type int and 'denominator' != 0"
    gcdOfFraction = gcd(abs(numerator), abs(denominator))
    assert isinstance(gcdOfFraction, int) and (numerator % gcdOfFraction == 0) \
        and (denominator % gcdOfFraction == 0), \
        "Error in function gcd(...,...)"
    return (numerator // gcdOfFraction, denominator // gcdOfFraction)


def factorial(n):
    assert isinstance(n, int) and (n >= 0), "'n' must been a int and >= 0"
    ans = 1
    for factor in range(1, n + 1):
        ans *= factor
    return ans


def fib(n):
    assert isinstance(n, int) and (n >= 0), "'n' must been an int and >= 0"
    tmp = 0
    fib1 = 1
    ans = 1
    for i in range(n - 1):
        tmp = ans
        ans += fib1
        fib1 = tmp
    return ans


if __name__ == "__main__":
    print("!!! Math Function !!!")
    print("1. Fibonacci Series\n2. Factorial\n3. Simplify Fraction\n4. Check Perfect Number\n5. Get Divisors\n6. Get Primes Between\n7. Get Prime\n8. kgV\n 9. GCD\n 10. Gold Bach\n11. Check if odd\n12. Check if Even\n13. Smallest Prime Factor\n14. Greatest Prime Factor\n15. Prime Numbers\n16. Sieve ER\n17. Check if Prime\n18. PI"))
    ch=int(input("Enter Your Choice For Following Functions::\t")
    
