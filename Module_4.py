# #Basic Conditional Statement
# my_password = 'password123'

# input_password = input('Please enter password: ')

# if input_password == my_password:
#     print('Access Granted')
# else:
#     print('Access Denied')

# #If-else Chain Example
# my_score = int(input('Please enter your grade: '))

# if my_score > 89:
#     my_grade = 'A'
# elif my_score > 79:
#     my_grade = 'B'
# elif my_score > 69:
#     my_grade = 'C'
# elif my_score > 59:
#     my_grade = 'D'
# else:
#     my_grade = 'F'

# print(my_grade)

#Create small calculator app
print('Welcome to calc-u-later. Please choose an operation:\n1- Addition\n2- Subtraction\n3- Multiplication\n4- Division')
input_operation = input()

input_num1 = float(input('Please enter your first number: '))
input_num2 = float(input('Please enter your second number: '))

if input_operation == '1':
    operation = '+'
    answer = input_num1 + input_num2
elif input_operation == '2':
    operation = '-'
    answer = input_num1 - input_num2
elif input_operation == '3':
    operation = 'x'
    answer = input_num1 * input_num2
elif input_operation == '4':
    operation = '/'
    if input_num2 == 0:
        input_num2 = float(input('Cannot divide by zero. Please enter a new number.'))
    answer = input_num1 / input_num2

print(f'The answer to {input_num1} {operation} {input_num2} is {answer:.2f}.')

#Using membership operators
my_list = ['Coke','Root Beer','Mountain Dew','Water','Lemonade','Milk','Dr. Pepper']

if 'Sprite' in my_list:
    print('Sprite is in the list')
else:
    print('Sprite is not in the list.')

#Logical Operators
##And- Both conditions are true
##Or- Either condition is true
##Not- Negates a condition

my_username = 'Pikachu25'
my_password = 'Electric100'

input_username = input('Please enter username: ')
input_password = input('Please enter password: ')

if input_username == my_username and input_password == my_password:
    print('Access Granted.')
elif input_username != my_username or input_password != my_password:
    print('Username and/or password is wrong')