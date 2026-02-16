"""
Program Name: Stages of Life - articipation activity
Aunthor: GMara
Purpose: this program determine a person's stages of life using if-elif-else statement
Ech condition checks a specific age range and prints the corresponding stage of life.
Date: 02/15/2026
"""

# Get the user's age then change the value to test other stages of life
age = 15 
if age < 2:
    print( "This person is a baby.")
elif age < 4:
    print( "This person is a toddler.")
elif age < 13:
    print( "This person is a kid")
elif age < 20:
    print( "This person is a teenager.")
elif age < 65:
    print( "This person is an adult.")
else :
    print( "This person is an elder.")