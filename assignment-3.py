# Asignment-3
Assignment 3(Python 3)

1.1 Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()

# my reduce function
def reduce_(func_,lst):
    result=lst[0]  # first item
    for item in lst[1:]:  # Next items
        result=func_(result,item)
        return result 
  print('add lst ' + str(myreduce(sum, [1,2,3])))

#1.2 Write a Python program to implement your own myfilter() function which works exactly like
#Python's built-in function filter()

def odd_check(n):  # make a function
    if n%2 !=0:
        return True
        
lst =range(20)

list(filter(odd_check,lst))

# 2 Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

mystring = "ACADGILD"
mystr_lst = [ strings for strings in mystring ]
print ("ACADGILD == " + str(mystr_lst))


#3. Implement a function longestWord() that takes a list of words and returns the longest one

from functools import reduce # import reduce function
words=['noah','lydia','mikael','girm','mizan'] # list of words
def mylongword(words):  #define function
    return reduce(lambda a,b: b if len(b)>len(a) else a,words) # finding longest work based on length
    print("the longest word from list is :" + mylongword(words)) # print longest word
