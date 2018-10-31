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

#wrtie list comprehensions to produce -> ['A', 'C', 'A', 'D', 'G', 'I', 'L', 'D']
mystring = "ACADGILD"
mystr_lst = [ strings for strings in mystring ]
print ("ACADGILD == " + str(mystr_lst))

#wrtie list comprehensions to produce -> ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
myinput_list = ['x','y','z']# input string
mynew_lst = [ i*n for i in myinput_list for n in range(1,5)]# comprehension list of lists
print("my new list --> " +   str(mynew_lst)) # print result

#wrtie list comprehensions to produce -> ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
myinput_list = ['x','y','z']# input string
mynew_lst = [ i*n for n in range(1,5) for i in myinput_list  ]# comprehension list of lists
print("my new list --> " +   str(mynew_lst))# print result

#wrtie list comprehensions to produce ->[[2], [3], [4], [3], [4], [5], [4], [5], [6]]

myinput_list = [2,3,4]# input numbers
mynew_lst = [ [i+n] for i in myinput_list for n in range(4)]# comprehension list of lists
print("my new list --> " +   str(mynew_lst))# print result

#wrtie list comprehensions to produce ->[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]


myinput_list = [2,3,4,5]# input numbers
mynew_lst = [ [i+n for i in range(4)] for n in myinput_list]# comprehension list of lists
print("my new list --> " +   str(mynew_lst))# print result

#wrtie list comprehensions to produce ->[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]


myinput_list = [1,2,3]# input numbers
mynew_lst = [(n,i) for i in range(1,4) for n in myinput_list]# comprehension list of lists
print("my new list --> " +   str(mynew_lst))# print result

#3. Implement a function longestWord() that takes a list of words and returns the longest one

from functools import reduce # import reduce function
words=['noah','lydia','mikael','girm','mizan'] # list of words
def mylongword(words):  #define function
    return reduce(lambda a,b: b if len(b)>len(a) else a,words) # finding longest work based on length
    print("the longest word from list is :" + mylongword(words)) # print longest word
