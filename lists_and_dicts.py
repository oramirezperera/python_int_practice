def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname': 'Orlando', 'lastname': 'Ramirez'}

    super_list = [
        {'firstname': 'Orlando', 'lastname': 'Ramirez'},
        {'firstname': 'Facundo', 'lastname': 'Garcia'},
        {'firstname': 'Miguel', 'lastname': 'Torres'},
        {'firstname': 'Susana', 'lastname': 'Martinez'}
    ]

    super_dict = {
        'natural_nums' : [1,2,3,4,5],
        'integer_nums' : [-1,-2,0,1,2],
        'floating_nums': [1.1,4.5,6.43]
    }

    for value in super_list:
        for key, value in value.items():
            print(f'{key} - {value}') 

if __name__ == '__main__':
    run()