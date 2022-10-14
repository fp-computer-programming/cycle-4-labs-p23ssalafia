# Author: Sean Salafia 10/13/22


#setting variables
sport = input("Find my favorite sport alphabetically: ")
#Setting conditionals to print certain statements if certain parameters are met.

if sport < "Ultimate Frisbee":
   print(sport + " comes before Ultimate Frisbee.")
elif sport > "Ultimate Frisbee":
   print(sport + " comes after Ultimate Frisbee.")
else:
   print("Ultimate Frisbee is the best sport")