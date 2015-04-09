#!/usr/bin/python    
'''
Created on Apr 9, 2015

@author: Blake Robertson
'''

# Addition Function 
def add(arg1, arg2):
    # Add both the parameters and return them 
    total = arg1 + arg2; 
    return total;

# Subtraction Function
def sub(arg1, arg2):
    # Subtract both the parameters and return them
    total = arg1 - arg2; 
    return total; 

# Multiplication Function
def mult(arg1, arg2):
    # Multiply both the parameters and return them
    total = arg1 * arg2;
    return total;

# Division Function
def div(arg1, arg2):
    # Divide both the parameters and return them
    total = arg1 / arg2;
    return total;

# Modulus Function
def mod(arg1, arg2):
    # Divides arg1 by arg2 then returns the remainder
    total = arg1 % arg2;
    return total;

# Exponential Function
def exp(arg1, arg2):
    # Performs exponential (power) calculation on operators
    total = arg1 ** arg2;
    return total;

# Math Functions Tests
total = add(10, 20);
print "Addition Total: ", total 
total = sub(20, 10);
print "Subtraction Total: ", total 
total = mult(10, 20);
print "Multiplication Total: ", total
total = div(30, 10);
print "Division Total: ", total
total = mod(30, 8);
print "Remainder Total: ", total
total = exp(30, 8);
print "Exponential Total: ", total
