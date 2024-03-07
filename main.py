#Python don't have direct approach to operate with fraction, so we are making our own

import math

class Fraction:
    def __init__(self,numerator, denominator):
        self.num=numerator
        self.den=denominator
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):
        final_den= self.den*other.den
        final_num= self.num*other.den + self.den*other.num

        gcd=math.gcd(final_num,final_den)
        return "{}/{}".format(int(final_num/gcd),int(final_den/gcd))
    
    def __sub__(self,other):
        final_den= self.den*other.den
        final_num= self.num*other.den - self.den*other.num

        gcd=math.gcd(final_num,final_den)
        if final_num==0:
            return "0"
        else:
            return "{}/{}".format(int(final_num/gcd),int(final_den/gcd))

    def __mul__(self, other):
        final_num=(self.num*other.num)
        final_den=(self.den*other.den)
        gcd=math.gcd(final_num, final_den)

        final_num //= gcd
        final_den //= gcd
        return "{}/{}".format(final_num,final_den)
    
    def __truediv__(self, other):
        final_num=(self.num*other.den)
        final_den=(self.den*other.num)
        gcd=math.gcd(final_num, final_den)

        final_num //= gcd
        final_den //= gcd
        return "{}/{}".format(final_num,final_den)
    
    def __eq__(self,other):
        if self.num==other.num and self.den==other.den:
            return "Both Fractions are equal"
        else: 
            return "Fractions are not equal!"
        
    def __lt__(self, other):
        if self.num * other.den < other.num * self.den:
            return f"{frac1} is lesser than {frac2}" 
        else:
            return f"{frac1} is not lesser than {frac2}" 

    def __gt__(self, other):
        if self.num * other.den > other.num * self.den:
            return f"{frac1} is greater than {frac2}"
        else:
            return f"{frac1} is not greater than {frac2}"

        
        

frac1= Fraction(12,15)
# print(frac1)
frac2= Fraction(12,15)

print(frac1*frac2)
print(frac1+frac2)
print(frac1-frac2)
print(frac1/frac2)
print(frac1==frac2)
print(frac1<frac2)
print(frac1>frac2)

#The greater and lesser than part are done this way just to distinguish the constructors and arraange the print functions like these

# can be also done like this


#     def __lt__(self, other):
#         return self.num * other.den < other.num * self.den

#     def __gt__(self, other):
#         return self.num * other.den > other.num * self.den


# if frac1 < frac2:
#     print(f"{frac1.num}/{frac1.den} is less than {frac2.num}/{frac2.den}")
# elif frac1 > frac2:
#     print(f"{frac1.num}/{frac1.den} is greater than {frac2.num}/{frac2.den}")
# else:
#     print(f"{frac1.num}/{frac1.den} is equal to {frac2.num}/{frac2.den}")
