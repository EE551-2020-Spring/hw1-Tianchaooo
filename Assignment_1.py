#!/usr/bin/python

"""
Python Core object Types
"""

import math


def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Assign a string "EE551" to a variable x
    x,y = "EE551", "Stevens"
    # y = "Stevens"
    # Assign a string "Stevens" to a variable y
    # Repeat variable y 5 times
    z = 5 * y
    # What is the length of z?
    length = len(z)
    # Concatenate variable y with string " is good"
    m = y + ' is good'
    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    n = m.replace('good','awesome')
    
    return x,y, z, length, m, n


def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"

    # Split variable n on a delimiter space into a list of substrings
    p=n.split(' ')
    # Get all the items past the first of the third substring
    r=p[2][1:]
    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    A=[[1, 4, 5],[6, 10, 11],[12, 17, 38]]
    # Collect the items in the last column of matrix A using list comprehension
    # Collect only the even items of the diagonal of matrix A using list comprehension
    c=A[2]
    d=[]
    for i in range(3):
        for e in A[i]:
            if e %2 ==0:
                d.append(e)
    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
    o=[]
    s='Stevens'
    for a in s:
        o.append(ord(a))
    return p, r, c, d, o


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    dic={'fruit':'apple','quantity':4,'color':"green"}
    # Get the item in dictionary f that the key "fruit" maps to
    a=dic['fruit']
    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    dic['quantity']= dic['quantity']+1
    f=dic['quantity']
    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    dic['name']={'first_name':"Grace",'last_name':"Hopper"}
    dic['jobs']=["scientist", "engineer"]
    dic['age']=85
    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    dic['jobs'].append("programmer")
    # Get the third job Grace has that you recently added
    p=dic['jobs'][2]
    # Use the sort() function to get sorted keys of amazing_grace in alphabetically ascending order
    k=sorted(dic.keys())
    return a, f, p, k

numbers_and_strings()
lists()
dictionaries()
