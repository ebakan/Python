#!/usr/bin/env python
def messup():
    import sys
    sys.exit('you tried to screw with my program')
    
def moneygen(terms, increment, interest):
    money=increment
    interest=interest/100+1
    for i in range(terms):
        money=money*interest+increment
    money-=increment
    totalspent=terms*increment
    totalmade=money-totalspent
    try:
        roi=totalmade/totalspent
    except ZeroDivisionError:
        roi=0       
    return round(money,2),round(totalspent,2),round(totalmade,2),round(roi,4)

def remoneygen(goal,interest,increment=0,terms=0):
    for i in (goal, interest):
        if i<=0:
            raise ValueError("Invalid goal of {0}".format(i))
    if increment and not terms:
        realinterest=interest/100+1
        money=increment*realinterest
        terms=1
        while money<=goal:
            money=(money+increment)*realinterest
            terms+=1
        return increment,terms
    elif terms and not increment:
        for i in range(goal):
            if moneygen(terms,i,interest)[0]>=goal:
                return i,terms
    else:
        raise ValueError("Must give either an increment or a time arguement")

def moneygenmain():
    args=input("Number of Terms, Increment, and Interest Rate:").split(',')
    if len(args)>3: messup()
    for i in range(3):
        try:
            float(eval(args[i]))
        except ValueError:
            messup()
        args[i]=eval(args[i])
    args[0]=int(args[0])
    money,totalspent,totalmade,roi=moneygen(args[0],args[1],args[2])
    print(
"""
Money Made:    ${0}
Total Spent:   ${1}
Total Made:    ${2}
ROI:            {3}%
""".format(money,totalspent,totalmade,roi*100))

def remoneygenmain():
    args=input("Goal, Interest Rate, Increment, and Number of Terms:"
               ).split(',')
    if len(args)>4: messup()
    for i in range(4):
        try:
            float(eval(args[i]))
        except ValueError:
            messup()
        args[i]=eval(args[i])
    args[2],args[3]=remoneygen(args[0],args[1],args[2],args[3])
    print("You must save a minimum of ${0} per term for {1} terms to reach a "\
          "goal of ${2} with {3}% interest.".format(
              args[2],args[3],args[0],args[1]))

def main():
        inp=input("Enter 0 for moneygen, or 1 for remoneygen:")
        if inp=='0':
            moneygenmain()
        elif inp=='1':
            remoneygenmain()
        else:
            messup()
    
if __name__=='__main__': main()
