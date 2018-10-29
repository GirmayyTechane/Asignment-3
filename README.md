# Asignment-3
Assignment 3(Python 3)


#1.2 Write a Python program to implement your own myfilter() function which works exactly like
#Python's built-in function filter()

def odd_check(n):  # make a function
    if n%2 !=0:
        return True
        
lst =range(20)

list(filter(odd_check,lst))
