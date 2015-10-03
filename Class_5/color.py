# This program displays the combination of two colors
# that are BLUE, RED, or YELLOW inputted by the user.

color1= input("Enter the color BLUE, RED, or YELLOW.  ").upper()
color2= input("Enter a different color that is BLUE, RED, or YELLOW. ").upper()

    
# These variables assign R,B,Y as False
#
red = False
blue = False
yellow = False
    
# These if statements will assign an R,B,Y variable as True
#
if color1 == "RED" or color2 == "RED":
    red = True
if color1 == "BLUE" or color2 == "BLUE":
    blue = True
if color1 == "YELLOW" or color2 == "YELLOW":
    yellow = True
if not red and not blue and not yellow:
    print('Please enter a color that is BLUE, RED, or YELLOW.')

# These if statements will display if two variables are True
#
if red and blue:
    print('Both colors combined create PURPLE.')
elif red and yellow:
    print('Both colors combined create ORANGE.')
elif blue and yellow:
    print('Both colors combined create GREEN.')
else:
    print('Both colors are the same.')

    