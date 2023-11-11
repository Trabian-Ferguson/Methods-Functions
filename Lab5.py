# Program Name: Lab5.py 
# Course: IT1114/Section 01
# Student Name: Trabian Ferguson
# Assignment Number: Lab5.py
# Due Date: 09/31/2023
# Purpose: This program calculates prime number with a starting number of 1 and a ending number of 37.

sn = int(input("Starting Number:"))
en = int(input("Ending Number:"))

def prime(a):
    if a <= 2:
        return True
    for i in range(2,a):
        if a%i==0:
            return False
    return True

for i in range(sn,en+1):
    if prime(i):
        print(i)



