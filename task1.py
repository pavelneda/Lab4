import math
class Rational:
    def __init__(self,numerator=1,denominator=1):
        self.numerator=numerator
        self.denominator=denominator
        self.__reducefraction()
        
    @property
    def numerator(self):
        return self.__numerator
        
    @numerator.setter
    def numerator(self,numerator):
        if not isinstance(numerator,int):
            raise TypeError("numerator must be integer")
        self.__numerator=numerator
        
    @property
    def denominator(self):
        return self.__denominator
        
    @denominator.setter
    def denominator(self,denominator):
        if not denominator:
            raise ZeroDivisionError("denominator must be not zero")
        if not isinstance(denominator,int):
            raise TypeError("denominator must be integer")
        self.__denominator=denominator
        
    def __reducefraction(self):
        k = math.gcd(self.numerator,self.denominator)
        if self.denominator<0:
            self.denominator=-self.denominator
            self.numerator=-self.numerator
        self.numerator=self.numerator//k
        self.denominator=self.denominator//k
        
    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'
        
    def floatingnumbers(self):
        return  float(self.__numerator)/self.__denominator
        
    def __add__(self,other):
        if isinstance(other,int):
            numerator=self.__numerator+self.__denominator*other
            denominator=self.__denominator
        elif isinstance(other,Rational):
            numerator=self.__numerator * other.__denominator + other.__numerator * self.__denominator
            denominator=self.__denominator * other.__denominator
        else:
            raise TypeError("other must be integer or Rational")
        return Rational(numerator,denominator)
        
    
    def __sub__(self,other):
        if isinstance(other,int):
            numerator=self.__numerator-self.__denominator*other
            denominator=self.__denominator
        elif isinstance(other,Rational):
            numerator=self.__numerator * other.__denominator - other.__numerator * self.__denominator
            denominator=self.__denominator * other.__denominator
        else:
            raise TypeError("other must be integer or Rational")
        return Rational(numerator,denominator)
        
    def __mul__(self,other):
        if isinstance(other,int):
            numerator=self.__numerator*other
            denominator=self.__denominator
        elif isinstance(other,Rational):
            numerator=self.__numerator * other.__numerator
            denominator=self.__denominator * other.__denominator
        else:
            raise TypeError("other must be integer or Rational")
        return Rational(numerator,denominator)
    
    def __truediv__(self,other):
        if isinstance(other,int):
            numerator=self.__denominator*other
            denominator=self.__denominator
        elif isinstance(other,Rational):
            numerator=self.__numerator * other.__denominator
            denominator=self.__denominator * other.__numerator
        else:
            raise TypeError("other must be integer or Rational")
        return Rational(numerator,denominator)
    
    def __iadd__(self,other):
        if isinstance(other,int):
            self.__numerator=self.__numerator + self.__denominator*other
        elif isinstance(other,Rational):
            self.__numerator=self.__numerator * other.__denominator + other.__numerator*self.__denominator
            self.__denominator=self.__denominator * other.__denominator
        else:
            raise TypeError("other must be integer or Rational")
        self.__reducefraction()
        return self
        
    def __isub__(self,other):
        if isinstance(other,int):
            self.__numerator=self.__numerator - self.__denominator*other
        elif isinstance(other,Rational):
            self.__numerator=self.__numerator * other.__denominator - other.__numerator*self.__denominator
            self.__denominator=self.__denominator * other.__denominator
        else:
            raise TypeError("other must be integer or Rational")
        self.__reducefraction()
        return self
    
    def __eq__(self,other):
        if isinstance(other,Rational):
            return self.floatingnumbers() == other.floatingnumbers()
        elif isinstance(other,(int,float)):
            return self.floatingnumbers() == other
        else:
            return False
    
    
    def __lt__(self,other):
        if isinstance(other,(int,float)):
            return self.floatingnumbers() < other
        elif isinstance(other,Rational):
            return self.floatingnumbers() < other.floatingnumbers()
        else:
            raise TypeError("can be compared only with integer,float,Rational")
    
    def __le__(self,other):
        if isinstance(other,(int,float)):
            return self.floatingnumbers() <= other
        elif isinstance(other,Rational):
            return self.floatingnumbers() <= other.floatingnumbers()
        else:
            raise TypeError("can be compared only with integer,float,Rational")
    
    
    def __gt__(self,other):
        if isinstance(other,(int,float)):
            return self.floatingnumbers() > other
        elif isinstance(other,Rational):
            return self.floatingnumbers() > other.floatingnumbers()
        else:
            raise TypeError("can be compared only with integer,float,Rational")
            
    def __ge__(self,other):
        if isinstance(other,(int,float)):
            return self.floatingnumbers() >= other
        elif isinstance(other,Rational):
            return self.floatingnumbers() >= other.floatingnumbers()
        else:
            raise TypeError("can be compared only with integer,float,Rational")


A=Rational(1,5)
B=Rational(1,5)
print("Floatint-point format(first): "+str(A.floatingnumbers()))
print("Floatint-point format(second): "+str(B.floatingnumbers()))
A=A+B
print(A)
A+=1
print(A)
print(A>B)
print(A==1)

