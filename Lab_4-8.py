#Author: Sean Salafia 10/20/22

#create variable for DNA and its complementary sequence
DNA = input('Input your 6 letter DNA sequence here: ')
Complimentary_Sequence = ""

if DNA[0] == "a":
    Complimentary_Sequence += "t"
elif DNA[0] == "t":
    Complimentary_Sequence += "a"
elif DNA[0] == "g":
    Complimentary_Sequence += "c"
elif DNA[0] == "c":
    Complimentary_Sequence += "g"

if DNA[1] == "a":
    Complimentary_Sequence += "t"
elif DNA[1] == "t":
    Complimentary_Sequence += "a"
elif DNA[1] == "g":
    Complimentary_Sequence += "c"
elif DNA[1] == "c":
    Complimentary_Sequence += "g"

if DNA[2] == "a":
    Complimentary_Sequence += "t"
elif DNA[2] == "t":
    Complimentary_Sequence += "a"
elif DNA[2] == "g":
    Complimentary_Sequence += "c"
elif DNA[2] == "c":
    Complimentary_Sequence += "g"

    
if DNA[3] == "a":
    Complimentary_Sequence += "t"
elif DNA[3] == "t":
    Complimentary_Sequence += "a"
elif DNA[3] == "g":
    Complimentary_Sequence += "c"
elif DNA[3] == "c":
    Complimentary_Sequence += "g"

        
if DNA[4] == "a":
    Complimentary_Sequence += "t"
elif DNA[4] == "t":
    Complimentary_Sequence += "a"
elif DNA[4] == "g":
    Complimentary_Sequence += "c"
elif DNA[4] == "c":
    Complimentary_Sequence += "g"

            
if DNA[5] == "a":
    Complimentary_Sequence += "t"
elif DNA[5] == "t":
    Complimentary_Sequence += "a"
elif DNA[5] == "g":
    Complimentary_Sequence += "c"
elif DNA[5] == "c":
    Complimentary_Sequence += "g"

print(Complimentary_Sequence)