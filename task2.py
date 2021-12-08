MIN_YEAR=1
MIN_MONTH=1
MAX_MONTH=12
MIN_DAY=1
DAYS_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Calendar:
        
    def __init__(self, year, month, day):
        self.year=year
        self.month=month
        self.day=day
    
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self,year):
        if not isinstance(year, int):
            raise TypeError("year type not correct")
        if not year >= MIN_YEAR:
            raise ValueError("year value not correct")
        self.__year=year
    
    @property
    def month(self):
        return self.__month
    
    @month.setter
    def month(self,month):
        if not isinstance(month, int):
            raise TypeError("month type not correct")
        if not MIN_MONTH <= month <= MAX_MONTH:
            raise ValueError("month not correct")
        self.__month=month
        
    @property
    def day(self):
        return self.__day
    
    @day.setter
    def day(self,day):
        days_in_month=29 if self.month == 2 and self.year % 4 ==0 and self.year % 100 !=0 or self.year % 400 == 0 else DAYS_MONTH[self.month]
        if not MIN_DAY <= day <=days_in_month:
            raise ValueError("day not correct")
        self.__day=day
        
    @property
    def date(self):
        return self.year,self.__month,self.__day
        
    def __str__(self):
        return f'{self.__year}.{self.__month}.{self.__day}'
    
    def __cmp(a,b):
        return 0 if a.date == b.date else 1 if a.date> b.date else -1
    
    def __eq__(self,second):
        if not isinstance(second,Calendar):
            raise TypeError("Type second not correct")
        return self.__cmp(second) == 0
    
    def __le__(self,second):
        if not isinstance(second,Calendar):
            raise TypeError("Type second not correct")
        return self.__cmp(second) <= 0
    
    def __lt__(self,second):
        if not isinstance(second,Calendar):
            raise TypeError("Type second not correct")
        return self.__cmp(second) < 0
    
    def __ge__(self,second):
        if not isinstance(second,Calendar):
            raise TypeError("Type second not correct")
        return self.__cmp(second) >= 0
    
    def __gt__(self,second):
        if not isinstance(second,Calendar):
            raise TypeError("Type second not correct")
        return self.__cmp(second) > 0
    
    def __ne__(self,second):
        if not isinstance(second,Calendar):
            raise TypeError("Type second not correct")
        return self.__cmp(second) != 0
    
    def __iadd__(self,second):
        if not isinstance(second,Calendar):
            raise TypeError("Type second not correct")
        day=self.__day+second.__day
        month=self.__month+second.__month
        year=self.__year+second.__year
        if day> DAYS_MONTH[self.__month]:
            day%=DAYS_MONTH[self.__month]
            month+=1
 
        if month>MAX_MONTH:
            month %=12
            year +=1
        
        self.__year=year
        self.__month=month
        self.__day=day
        return self
    
    def __isub__(self,second):
        if not isinstance(second,Calendar):
            raise TypeError("Type second not correct")
        day=self.__day-second.__day
        month=self.__month-second.__month
        year=self.__year-second.__year
        
        if day<MIN_DAY:
            month-=1
            day=DAYS_MONTH[month]+day
        
        if month<MAX_MONTH:
            year-=1
            month=12
        self.__year=year
        self.__month=month
        self.__day=day
        return self
    
    
        
one=Calendar(2021,7,3)
two=Calendar(2020,8,31)
three=Calendar(1,2,3)
print(one)
print(one>two)
print(one!=three)
two+=three
print(two)
