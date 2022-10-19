#Author: Sean Salafia 10/18/22

#input animal and food names
Creature_with_living_properties = input('Input Animal Here: ')
Consumable_Matter = input('Input Food Here: ')

#search for the first letter of each word and print it

First_letter_of_animal = Creature_with_living_properties[0]
print(First_letter_of_animal)

First_letter_of_food = Consumable_Matter[0]
print(First_letter_of_food)

Last_letter_of_food = Consumable_Matter[-1]
print (Last_letter_of_food)


#conditional statement checking for similarity of the first letters

if First_letter_of_animal == (First_letter_of_food) and (First_letter_of_animal) == (Last_letter_of_food):
    print ('The Beast May Enter the Feast')
else:
    print ('The Beast may NOT enter the Feast')





#if First_letter_of_animal == First_letter_of_food:
#    if First_letter_of_food == Last_letter_of_food:
#        print ('The Beast May Enter the Feast')
#else:
#    print ('The Beast may not enter the Feast')

