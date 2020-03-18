

def get_prime_number():
    prime_numbers = []
    candidate = 2
    while True:
        if candidate <= 3:
            prime_numbers.append(candidate)
            yield candidate
        
        is_prime = True
        for prime_num in prime_numbers:
            if candidate % prime_num == 0:
                is_prime = False
                break
        
        
        if is_prime:
            prime_numbers.append(candidate)
            yield candidate

        candidate += 1

def main():
    while True:
        try:
            input_range = int(input('Insert how many prime numbers do you want to return: '))
            if input_range <= 0:
                raise ValueError
        except:
            print('Invalid number. Insert a valid number, please.')
        else:
            break
    
    gen_prime_number = get_prime_number()
    prime_output = open('prime_output.txt', 'w+')
    for _ in range(input_range):
        prime_output.write(str(next(gen_prime_number)) + '\n')

    prime_output.close()

if __name__ == '__main__':
    main()
