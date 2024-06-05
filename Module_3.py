#Get the length of a string
my_string = 'blue'
print(len(my_string))

#Get a specific character from a string
print(my_string[2])

#Format numbers to look better using f-strings
my_num = 52849.4958
print(f'using f\t\t{my_num:f}')
print(f'using .2f\t{my_num:.2f}')
print(f'using .3f\t{my_num:.3f}')

#Create a list of strings
my_string_list = ['Taco','Pizza','Burger']
print(my_string_list[0])

#Create a list of integers
my_int_list = [200,35,47]
print(my_int_list[1] + my_int_list[2])

#Create a list of multiple types
my_mixed_list = ['Peanut Butter',42,4.2,False]
print(f'I ate {my_mixed_list[1]} jars of {my_mixed_list[0]} I am now {my_mixed_list[2]} times my orginal size. That statement was {my_mixed_list[3]}.')

# #Add items to a list
# pokemon_list = ['Squirtle','Koffing','Fletchling','Wooper']
# pokemon_list.append(input('What is your favorite pokemon?\n'))
# print(pokemon_list)

# #Remove items from a list
# pokemon_list.remove(input('Who do you hate?\n'))
# print(pokemon_list)

# #Pop items from a list
# pokemon_list.pop(int(input('Which pokemon number do you want to remove?'))-1)
# print(pokemon_list)

#Create a set
my_set = {'Goose','T-Rex','Hippo','Goose'}
my_set.add('Hippo')
print(my_set)

#Create a dictionary
dog_dict = {'Gender'    :   'Female',
            'Size'      :   'Small',
            'Age'       :   6,
            'Legs'      :   4,
            'Breed'     :   'Puggle'}

print(f'The dog is a {dog_dict['Breed']}.')

#Create a list of dictionaries
dog_dict_2 = {'Gender'    :   'Male',
            'Size'      :   'Large',
            'Age'       :   2,
            'Legs'      :   3,
            'Breed'     :   'German Shepherd'}

dog_list = [dog_dict,dog_dict_2]

print(f'The dog is {dog_list[1]['Age']} years old')

#Add an item to a dictionary
dog_dict['Color'] = 'Brown'
print(dog_dict['Color'])