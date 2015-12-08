# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:33:27 2015
@author: ryan


The following is a coding problem I received during an interview.

Given two strings of only zeros and ones e.g., '01101' and '101',
perform binary addition on the two and return the output.

Constraints: don't use the native binary addition functions, and don't just
convert the binary string to base ten and add it.

Use only the built-in python library. 
"""

def binaryadd(s1,s2):
    '''
    s1 and s2 should the binary strings. Expects a binary string. 
    returns the sum of the the two binary numbers as a string    
    '''    
    #initialization
    cur_carry = 0 #initialize the first carry to zero for the very first place
    ls1_r = list(s1)[::-1] #reverse strings so we start addings the first values
    ls2_r = list(s2)[::-1]
    bsum = list() #make an empty list that we'll add values to
    v1_emp = 0 #values to check and make sure the string lists are not empty
    v2_emp = 0
    
    while True:  
        '''
        loop through each place, and add the values for each string, along with 
        any previous carry values. If both strings are exhausted, and there
        are no more carry values, then terminate the loop.
        '''
        if len(ls1_r) > 0 and not v1_emp:
            '''
            pop the first value in both lists of numbers to compare
            but if the list is empty, that place is just 0, and note that 
            that value is empty
            '''
            v1 = int(ls1_r.pop(0)) 
            v1_emp = 0 
        else:
            v1 = 0
            v1_emp = 1
    
        if len(ls2_r) > 0 and not v2_emp:
            v2 = int(ls2_r.pop(0))
            v2_emp = 0
        else:
            v2 = 0
            v2_emp = 1
        
        if v1_emp and v2_emp and cur_carry == 0:
            break
        
        cur_sum = v1 + v2 + cur_carry #addition here
        cur_place =  cur_sum % 2
        cur_carry = cur_sum / 2
        bsum.append(cur_place) #append to the list of cur place values
    
    bsum_out = bsum[::-1] #since the list of values is in reverse order, re-reverse it
    bsum_str = ''.join([str(x) for x in bsum_out]) #make into a string
    return bsum_str

    
'''
institute checks
'''    
if __name__ == '__main__':
    in_s1 = '11111'
    in_s2 = '111'
    print(binaryadd(in_s1,in_s2))