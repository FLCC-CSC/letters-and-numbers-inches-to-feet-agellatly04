# FILE NAME - inches_to_feet.py
# DRG - Rerun for points 2025-02-18-2347
# NAME: Andrew Gellatly
# DATE: 2/18/2025
# BRIEF DESCRIPTION:  A program that converts inches to feet.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience





# BEWARE! You'll need to cast not only the input from the user
# but also maybe the number of feet

########## ENTER YER CODE BELOW THIS LINE ##########
    
inches = int(input('Enter the number of inches: '))
feet = inches // 12
feetR = inches % 12
    
print(f'{inches} inches is {feet} feet, and {feetR} inches')
    
########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the number of inches: 14

14 inches is 1 feet, and 2 inches


'''



'''

Enter the number of inches: 100

100 inches is 8 feet, and 4 inches

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does it mean to "cast" input from the user?

It means to convert user input from one data type to another.




'''
