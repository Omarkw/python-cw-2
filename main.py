my_name = input('whats your name?')
my_age = int(input('whats you age?'))
print(f'my name is {my_name} and I am {my_age} years old')


first_number = int(input('first number:'))
second_number = int(input('second number:'))
operation = input('the operation:')
if operation == '+':
    print(first_number + second_number)
elif operation == '-':
    print(first_number - second_number)
elif operation == '*':
    print(first_number * second_number)
elif operation == '/':
    print(first_number / second_number) 
else:
    print('the operation is invalid')

bus_capacity = 20
number_of_people = int(input('how many people?'))
number_of_want = int(input('how many people want to go school?'))
empty_sets = bus_capacity - number_of_people
if empty_sets >= number_of_want:
    print('there is space in bus')
else:
    print('the bus is full')






