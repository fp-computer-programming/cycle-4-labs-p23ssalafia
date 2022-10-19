#Author: Sean Salafia 10/14/22

from operator import index

#define variables
word = 'flibbertigibbet'
#find letter and print index of that letter
find_t = word.find("t")
print (find_t)

#find and print the letter after the 8th index
Eighth_letter = word[8:9]
print(Eighth_letter)

#creatie variable for my first name
first_name_lowercase = 'sean'
my_name_uppercase = first_name_lowercase.upper()
print(my_name_uppercase)

#Use split to add a space to where each comma is.
sentence = "I wish, I wish, I was a fish."
split_sentence = sentence.split(',')
print(split_sentence)
