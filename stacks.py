# CS 107, Fall 2018 -- Project 5
# Imperative Data and Stacks
from library import *
import doctest

class StackUnderflow(Exception):
    pass

# Create an empty stack, whose length is numElements
def make_stack(numElements):
    return [0, [None] * numElements, numElements]

# Does s "look like" a stack
def looksLikeStack(s):
    return len(s) == 3 and type(s[0]) == type(0) and type(s[1]) == type([]) and type(s[2]) == type(0)

# Three accessor functions for stacks
def top(stack): 
    precondition(looksLikeStack(stack))
    return stack[0]

def data(stack): 
    precondition(looksLikeStack(stack))
    return stack[1]

def size(stack): 
    precondition(looksLikeStack(stack))
    return stack[2]

# Return a new copy of the stack, without changing anything
def copyStack(s):
    precondition(looksLikeStack(s))
    newArray = [None] * size(s)   #define a newArray, the same size as stack
    for i in range(size(s)):      #iterate through the old stack, building up newArray
        newArray[i] = s[1][i]     #take each element from the old stack, and assign it to newArray
    postcondition(len(newArray) == size(s))
    return [s[0], newArray, s[2]] #return a stack, with the newArray          

    
# Push an element onto a stack
def push(stack, e):
    precondition(looksLikeStack(stack))
    if (top(stack) >= size(stack)):
        # Reallocate
        newSize = size(stack) * 2
        newData = [None] * newSize
        i = 0
        # Copy old data
        while (i < size(stack)):
            newData[i] = data(stack)[i]
            i = i + 1
        # Add new element
        newData[i] = e
        # Set up stack correctly again
        stack[0] = top(stack) + 1
        stack[1] = newData
        stack[2] = newSize
    else:
        # Add to top of stack and increment "top of stack"
        stack[1][top(stack)] = e
        stack[0] = top(stack) + 1

# Pop the top element from the stack
def pop(stack):
    
    newArray = copyStack(stack) #create a newArray that is an exact copy of the stack. 
    precondition(looksLikeStack(stack))

    if isEmpty(stack): #raise a StackUnderFlowException if stack has no elements in it
        raise StackUnderFlowExeception
    else:
        #Replace "popped" element (top of stack) with 'None'
        #Decrease the value representing where the top of the stack is.
        stack[1][top(stack) - 1] = None
        stack[0] = top(stack) - 1       

    return newArray[1][top(newArray)-1]   #return the top of the stack


#Takes a stack as an argument and returns an array representing the stack as an array.
#Must remove all unused elements.
def toArray(stack):
    precondition(looksLikeStack(stack))

    newArray = [None] * stack[0]        #define a newArray, with size of the stack[0]
    for i in range(top(stack)):         #iterate through the stack
        if i != None:                   #As long as the element is not unused..
            newArray[i] = stack[1][i]   #Assign the value to newArray
    postcondition(type(newArray) == type([]))
    return newArray                     #return the array
    
    
#This function reverses a stack. The empty space in the array must be left alone.
def reverse(stack):
    precondition(looksLikeStack(stack))
    
    newArray = [None] * stack[2]                     #define a newArray, the same size as the stack
    for i in range(stack[0]):                        #Note that we iterate in the range of stack[0], as to leave empty space untouched.
        newArray[i] = stack[1][top(stack) - (i + 1)] #Go "backwards", reassigning each element in the old array to the new array
    stack[1] = newArray
    stack = [stack[0], stack[1], stack[2]]           #reassign stack as with newArray

    postcondition(looksLikeStack(stack))
    return stack
    

#This is a helper function that counts how many "None"'s occur in
#an array.
def countNone(stack):
    precondition(looksLikeStack(stack))
    """
    >>> countNone([3, [1,2,3,None, None, None],6])
    3

    >>> countNone()
    0

    >>> countNone([4, [3,6,9,12], 4]
    0

    >>> countNone([0, [None], 1])
    1

    """
    y = 0                 #define a variable to eventually increment. 
    if isEmpty(stack[0]): #if the stack is empty, return 0. There are no "None"'s.
        return 0  
    else:
        for i in stack[1]: 
            if i == None: #if the element is a "None"..
                y = y+1   #increment y by 1
    postcondition(type(y) == int)
    return y              #return y

#This function inserts an element e into a list, such that the list remains sorted.
def insert(lst, e):
    precondition(type(lst) == type([]))
    precondition(type(e) == int)
    
    """    
    >>> insert([1,2,None,None], 3)
    [1, 2, 3, None]

    >>> insert([None], 8)
    [8]

    >>> insert([], 5)
    [5]
    
    """
    #Note: This function assumes that there is a "None" in the list,
    #otherwise a merging won't work anyway, because there won't be space to merge.
    #It still works if a list does not contain a 'None' though.
    
    if isEmpty(lst):            #if the list is empty, return a list containing only e
        return [e]
    if head(lst) == None:       #if the head of the list is a 'None'...
        return [e] + lst[:-1]   #"replace" the None with 'e' by returninf a list of [e] and removing the last element in the list.
    if head(lst) >= e:          #if the head of the list is greater than e, 
        return [e] + lst[:-1]   #return a list with e at the front.
    else: 
        return [head(lst)] + insert(tail(lst), e) #otherwise, return the head of the list, and recurse on the rest of the list.

#This function merges s1 and s2, using the helper function 'insert.'
#It works by inserting each element from s2's array into s1's array one at a time.    
def merge(s1,s2):
    precondition(looksLikeStack(s1))
    precondition(looksLikeStack(s2))
    
    #First, check if s1 is large enough to accommodate the elements from s2:
    if countNone(s1) < size(s2): #if the amount of 'None's in s1 is less than the size of s2...
        raise IndexError         #raise an index error
    else:
        x = s1[1]                #assign x to the array in stack 1
        for i in s2[1]:          #iterate through each element in the stack 2's array
            x = insert(x, i)     #insert i into the array, assign the newly 'sorted' array to x
        s1[0] = (s1[0]+s2[0])    #For this step, I replace each index in s1 individually to create a new stack.
        s1[1] = x
        s1[2] = s1[2]
        postcondition(looksLikeStack(s1))
        return s1                #return the altered s1

