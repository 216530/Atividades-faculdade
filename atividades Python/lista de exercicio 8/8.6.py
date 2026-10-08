def eh_primo(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


print(eh_primo(2))
print(eh_primo(17))
print(eh_primo(20))
print(eh_primo(1))
print(eh_primo(-7))