def factorize(n: int) -> List[int]:
    factors = []
    i = 2
    while i <= n:
        if n % i != 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    return factors

print(factorize(8))
print(factorize(25))
print(factorize(70))