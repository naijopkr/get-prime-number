from get_prime_number import get_prime_number

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
