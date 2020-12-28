
#####################################################################################################
'''     
                    Author--------
                    Name: Hemant Jain             Final Year Student
                    Poornima Institute of Engineering and Technology, Jaipur
                    
                    *******************Python Coder*************************
'''                                                                                
######################################################################################################

import sys
import time as mt,bisect,sys
import math
from sys import stdin,stdout
from collections import deque
from fractions import Fraction
from collections import Counter
from collections import OrderedDict


def si():   return int(sys.stdin.readline())                        #integer input
def st():   return stdin.readline()                                 #string input
def mi():   return map(int, sys.stdin.readline().split())           #multiple integer input 
def lis():  return list(map(int, sys.stdin.readline().split()))     #list input

def lcm(list1,string2):   return (list1*string2)//gcd(list1,string2)                              # to calculate lcm

def gcd(list1,string2):                                                       # to calculate gcd
    if list1==0:
        return string2
    elif string2==0:
        return list1
    if list1>string2:
        return gcd(list1%string2,string2)
    else:
        return gcd(list1,string2%list1)

def isPrime(n) : 
	if (n <= 1) : 
		return False
	if (n <= 3) : 
		return True
	if (n % 2 == 0 or n % 3 == 0) : 
		return False
	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6
	return True

test=si()
for _ in range(test):
    x,y,k,n=mi()
    count=abs(y-x)/(2.0*k)
    if(math.floor(count)==math.ceil(count)):
        print("Yes")
    else:
        print("No")
