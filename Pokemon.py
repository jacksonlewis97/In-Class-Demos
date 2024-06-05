#Import Libraries
import pokebase as pb

#Get pokemon from user
input_pokemon = input('Please enter the name of a pokemon: ').lower()

#Make API call
pokemon = pb.APIResource('pokemon',input_pokemon)

#Display data
print(f'Name:\t{str(pokemon.name).capitalize()}')
print(f'Height:\t{pokemon.height / 10} m')
print(f'Weight:\t{pokemon.weight * 10} kg')

if len(pokemon.types) == 1:
    print(f'Type:\t{str(pokemon.types[0].type.name).capitalize()}')
else:print(f'Type:\t{str(pokemon.types[0].type.name).capitalize()}/{str(pokemon.types[1].type.name).capitalize()}')
    