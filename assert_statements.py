def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors


def run():
    num = input('Enter a number ')
    assert num.isnumeric(), 'you need to type a number'
    print(divisors(int(num)))
    print(divisors(num))
    print('Program ended')
    

if __name__ == '__main__':
    run()