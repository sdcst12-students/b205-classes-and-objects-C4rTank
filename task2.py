#!python3
"""
Compound Interest Calculator
Create a class object that accepts paramters for Principal, Annual Interest Rate, Number of compounding periods.  
Create a class method that calculates the amount of compound interest for a given length of time.

Extension: accept time given in different measurements, but convert them to years for use in your class template.
"""


class Calc:
    principal = 0
    rate = 0
    nPeriods = 0

#------------------------------------

    def __init__(self,P,r,n):
        self.P = P
        self.r = r
        self.n = n
        return
    
#------------------------------------
    
    def interest(self,t):
        
        r = self.r/100

        I = (1 + r /self.n)
        
        P = self.n * t
        
        I = I**P
        I = I * self.P
        I = I - self.P

        I = round(I,2)
        print(I)
        return I

#------------------------------------

    def amount(self,t):
        
        r = self.r/100

        I = (1 + r /self.n)
        
        P = self.n * t
        
        I = I**P
        I = I * self.P

        I = round(I,2)
        print(I)
        return I

#------------------------------------

a = Calc(P=1000,r=4,n=2)
assert a.interest(3) == 126.16
assert a.amount(5) == 1218.99

b = Calc(P=5000,r=5.25,n=12)
assert b.interest(10) == 3442.62

#DONE

