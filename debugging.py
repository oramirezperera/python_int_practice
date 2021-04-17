def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors


def run():
    try:
        num = int(input('Enter a number '))
        if num < 0:
            raise ValueError
            print('You need to type a positive number')
        print(divisors(num))
        print('Program ended')
    

    except ValueError:
        print('You need to type a number')


if __name__ == '__main__':
    run()