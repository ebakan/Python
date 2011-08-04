#!/usr/bin/env python
#Generates all slots digit numbers which are made up of each number in items
def gennums(slots, items):
	if slots==1:
		return items
	else:
		return [k+i for k in items for i in gennums(slots-1,items)]

#filters a given list in which all numbers use the digits 1-6 once
def genpositive(x):
    return list(filter(lambda i: '1' in i and '2' in i and '3' in i and '4' in i and '5' in i and '6' in i, x))

#for a given list and a given step, returns a list of numbers where the number formed by the first step digits is divisible by step
def filterdigits(lst,step):
    return list(filter(lambda x: int(x[:step])%step==0,lst))

#main program
def main():
    #creates a list of numbers which use the digits 1-6 one time each
    n=genpositive(gennums(6,[str(i+1) for i in range(6)]))
    #calls the filterdigits function each time from numbers 2 to 6 to return the correct answers
    for i in range(2,7):
        n=filterdigits(n,i)
    for i in n:
        #returns solutions
        print(i)

#just tester code
if __name__=='__main__':
    main()
