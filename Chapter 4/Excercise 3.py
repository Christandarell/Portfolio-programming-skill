# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 03:33:34 2023

@author: darel
"""
#chapter 4
#Exercise 3: Alien Colors #3
alien_color = input("Enter the alien's color (green, yellow, or red): ")
# Get the alien's color as input
if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points for shooting the yellow alien.")
elif alien_color == 'red':
    print("Congratulations! You just earned 15 points for shooting the red alien.")
else:
    print("Unknown alien color. Please enter 'green', 'yellow', or 'red'.")
