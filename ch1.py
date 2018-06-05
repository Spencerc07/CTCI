#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 19:50:02 2018

@author: spencer
"""

#1 isUnique - Determine if a string has all unique characters
def isUnique(string):
    string = string.lower()
    contained = {}
    for letter in string:
        if letter in contained:
            return False
        else:
            contained[letter] = True
    return True
    
isUnique("heLlo")

#Implemented with no additional data structure
def isUnique_noDS(string):
    string = sorted(string.lower())
    for x in range(len(string)-1):
        if string[x] == string[x+1]:
            return False
    return True

isUnique_noDS("Michael")
    
#2 Check Permutation - Determine if string one is a permutation of string two
def checkPermutation(one, two):
    if (len(one) != len(two)):
        return False
    one = sorted(one)
    two = sorted(two)
    a = 0
    for a in range(len(one)):
        if (one[a] != two[a]):
            return False
    return True

checkPermutation("baby", "abby")

#3 URLify = Method to replae all spaces with %20. Trivial in python.
def URLify(string):
    return string.replace(' ', '%20')

URLify('spencer james christensen')

#4 Palindrome Permutation - Given a string, check to see if it's a permutation of a palindrome

def palindromePermutation(string):
    string = string.lower()
    letters = {}
    for letter in string:
        if letter in letters:
            letters[letter] = letters[letter] + 1
        else:
            letters[letter] = 1
    token = 0
    for count in letters.values():
        if count % 2 != 0:
            if token != 0:
                return False
            else:
                token = 1
    return True
            
palindromePermutation("baba")
palindromePermutation("carrace")

#5 One Away = Determine if two strings are one edit away from eachother
def oneAway(one, two):
    if (len(one) == len(two)):
        return oneAwayReplace(one, two)
    elif (len(one) + 1 == len(two)):
        return oneAwayInsert(one,two)
    elif (len(one) == len(two) + 1):
        return oneAwayInsert(two, one)
    return False

def oneAwayReplace(one, two):
    difference = False
    counter = 0
    while counter < len(one):
        if(one[counter] != two[counter]):
            if(difference):
                return False
            difference = True
        counter = counter + 1
    return True

def oneAwayInsert(one, two):
    index1 = 0
    index2 = 0
    while(index2 < len(two) and index1 < len(one)):
        if one[index1] != two[index2]:
            if index1 != index2:
                return False
            
            index2 += 1
            
        else:
            index1 += 1
            index2 += 2
    return True

        
oneAway('pale', 'bake')
oneAway('peas', 'paes')

#6 String Compression - compress a string using counts of a letter
#e.g. aabbbbbbc = a2b6c1
def stringCompression(string):
    compressed = []
    consecutive = 0
    counter = 0
    
    while counter < len(string):
        consecutive += 1
        if(counter+1 >= len(string) or string[counter] != string[counter+1]):
            compressed.append(string[counter])
            compressed.append(str(consecutive))
            consecutive = 0
        counter += 1
    compressed = ''.join(compressed)
    return compressed

stringCompression("aaabbbbbbbbccaad")

#7 Rotate Matrix - given a nxn matrix, rotate it 90 degrees. In-plae method
def rotateMatrix(matrix):
    #layer approah. start with n/2 layers. 
    #rotate outer shells
    if len(matrix) != len(matrix[0]):
        print("not an nxn matrix")
        return matrix
    
    n = len(matrix)
    r = n//2
    layer = 0
    
    while layer < r:
        first = layer
        last = n-1-layer
        
        i = first
        while i < last:
            offset = i - first
            top = matrix[first][i]
            
            #swap left to top
            matrix[first][i] = matrix[last-offset][first]
            
            #swap bottom to left
            matrix[last-offset][first] = matrix[last][last - offset]
            
            #swap right to bottom
            matrix[last][last-offset] = matrix[i][last]
            
            #top to right
            matrix[i][last] = top
            
            i += 1
        layer += 1
        
    return matrix

mat = [[1,2,3],[4,5,6],[7,8,9]]
    
rotateMatrix(mat)
    
#8 Zero Matrix - if an element in a MxN matrix is 0, set it's row and column to zero

def zeroMatrix(matrix):
    #store all rows and columns that have a zero
    zeroRows = []
    for i in range(len(matrix)):
        zeroRows.append(False)
    zeroCols = []
    for i in range(len(matrix[0])):
        zeroCols.append(False)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zeroRows[i] = True
                zeroCols[j] = True
    
    for i in range(len(matrix)):
        print("i= ", i)
        if zeroRows[i]:
            for j in range(len(matrix[0])):
                print("j= ", j)
                matrix[i][j] = 0

    return matrix
    
    
mat = [[1,2,3,4], [6,0,1,2], [1,1,9,0], [3,6,5,8], [4,1,4,8]]
zeroMatrix(mat)
print(len(mat))
print(len(mat[0]))    
    
    
#9 - String Rotation
def stringRotation(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if(len(s1) == len(s2) and len(s1) > 0):
        s1s1 = s1 + s1
        return s2 in s1s1
    return False
    
stringRotation("teaset", "asette")
stringRotation("teaset", "asetTe")
stringRotation("Blue","Red")
stringRotation("Able", "able")
    

"""
Interview Demo - Given a string S and a number K, group S so that each
group is K characters long, seperated by a dash (-). The first group may be
any length equal or less than K. S is guarnteed to be alphanumeric, and
contains dashes in random locations.
"""
def solution(S, K):
    S = S.replace('-', '')
    S = S.upper()
    
    if (K >= len(S)):
        return S
    
    end = len(S)-1
    
    dashes = len(S)//K
    if len(S)%K == 0 and dashes > 0:
        dashes -= 1
    
    for i in range(dashes+1):
        if i > 0:
            S = S[:end-K*i+1] + "-" + S[end-K*i+1:]
        
    return S


solution('3a-arre-e43f', 3)
solution('er23-234ddsd-34343dgthgtyh-45-bfgbfg5-54646', 5)
solution('eereqdvkkfbjherfherkfgvZX>Kcjvasfi', 9)
solution('erwd-12', 10)




x="hello"
print(x[0].islower())


def swap_case(s):
    a = list(s)
    for x in range(len(s)):
        if s[x].islower():
            a[x] = s[x].upper()
        elif s[x].isupper():
            a[x] = s[x].lower()
    return str(a)

swap_case("heLlO")