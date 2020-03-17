PRIME_NUMBERS = []

def get_prime_number():
    candidate = 2
    while True:
        if candidate <= 3:
            PRIME_NUMBERS.append(candidate)
            yield candidate
        
        is_prime = True
        for prime_num in PRIME_NUMBERS:
            if candidate % prime_num == 0:
                is_prime = False
                break
        
        
        if is_prime:
            PRIME_NUMBERS.append(candidate)
            yield candidate

        candidate += 1

foo = get_prime_number()
for n in range(20):
    print(next(foo))
