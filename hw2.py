""" create a dictionary with the first thousand numbers and their square root"""
from math import sqrt

def run():
    my_dict = {i: sqrt(i) for i in range(1,1001)}
    print(my_dict)

if __name__ == '__main__':
    run()