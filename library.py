# Helper Functions for Project 3
# CMSC 107 -- Fall 2018
# Done by Kristopher Micinski

# DO NOT edit this file

class UnimplementedExeception(Exception):
    pass

class PreconditionException(Exception):
    pass

class PostconditionException(Exception):
    pass

# 
# List Basics
# 
def isEmpty(lst): return lst == []
def head(lst): return lst[0]
def tail(lst): return lst[1:]

# Does list lst contain the member x
def contains(lst, x): return x in lst

# Helper function for forall
def forallHelper(lst,f,i):
    if (i >= len(lst)): return True
    else: return f(lst[i]) and forallHelper(lst,f,i+1)

# Does f hold for every element of lst
def forall(lst, f):
    return forallHelper(lst,f,0)

# Helper function for forall
def existsHelper(lst,f,i):
    if (i >= len(lst)): return False
    else: return f(lst[i]) or existsHelper(lst,f,i+1)

# Does f hold for every element of lst
def exists(lst, f):
    return existsHelper(lst,f,0)

#
# Decorator-based pre/postconditions
#

# Code that allows wrapping functions
import functools

def precondition(check):
    if (not check):
        raise PreconditionException

def postcondition(check):
    if (not check):
        raise PostconditionException

