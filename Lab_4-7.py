#Author: Sean Salafia 10/19/22

#input variables and having them as strings and integers
first_number = input('Input First Number Here ')
second_number = input('Input Second Number Here ')
third_number = input('Input Third Number Here ')
fourth_number = input('Input Fourth Number Here ')
fifth_number = input('Input Fifth Number Here ')

int(first_number)
int(second_number)
int(third_number)
int(fourth_number)
int(fifth_number)

#Making the input integers and adding spaces
print(first_number+' '+second_number+' '+third_number+' '+fourth_number+' '+fifth_number)

#Find the largest and smallest numbers
Largest_Number = max(first_number,second_number,third_number,fourth_number,fifth_number)
Smallest_Number = min(first_number,second_number,third_number,fourth_number,fifth_number)
print("Largest number given was "+Largest_Number)
print("Smallest number given was "+Smallest_Number)

int(Largest_Number)
int(Smallest_Number)

#Multiply the largest and smallest numbers
Product = int(Largest_Number) * int(Smallest_Number)
int(Product)
str(Product)
print("The product of the two extracted numbers is " +str(Product))

