import re


class Circle :
    def __init__(self,radius,) -> None:
        self.radius=radius
        self.length=3.14*radius

    def __eq__(self, other):
        if self.radius== other.radius:
            return True
        else :
            return False
        
    def __lt__(self, other):
        if self.length<other.length:
            return True
        else :
            return False
        
    def __le__(self, other):
        if self.length<=other.length:
            return True
        else :
            return False
        
    def __gt__(self, other):
        if self.length>other.length:
            return True
        else :
            return False
        
    def __ge__(self, other):
        if self.length>=other.length:
            return True
        else :
            return False 
        
    def __add__(self, other):
        return self.radius + other
    
    def __mul__(self, other):
        return self.radius - other
    
    def __iadd__(self, other):
        self.radius = self.radius + other
        return self.radius
    
    def __isub__(self, other):
        self.radius=self.radius - other
        return self.radius

    
class Airplane :
    def __init__(self,type_of_aircraft,number_of_passengers) -> None:
        self.type_of_aircraft=type_of_aircraft
        self.number_of_passengers=number_of_passengers

    def __eq__(self, other):
        if self.type_of_aircraft == other.type_of_aircraft:
            return True
        else:
            return False
        
    def __add__(self, other):
        return self.number_of_passengers + other
    
    def __mul__(self, other):
        return self.number_of_passengers - other
    
    def __iadd__(self, other):
        self.number_of_passengers = self.number_of_passengers + other
        return self.number_of_passengers
    
    def __isub__(self, other):
        self.number_of_passengers = self.number_of_passengers - other
        return self.number_of_passengers
    
    def __lt__(self, other):
        if self.number_of_passengers<other.number_of_passengers:
            return True
        else:
            return False
    def __le__(self, other):
        if self.number_of_passengers <= other.number_of_passengers:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.number_of_passengers > other.number_of_passengers:
            return True
        else:
            return False
    
    def __ge__(self, other):
        if self.number_of_passengers >= other.number_of_passengers:
            return True
        else:
            return False
        


class Flat:
    def __init__(self,price,area) -> None:
        self.price=price
        self.area=area
    
    def __eq__(self, other):
        if self.area==other.area:
            return True
        else: return False

    def __ne__(self, other):
        if self.area!=other.area:
            return True
        else: return False
    
    def __lt__(self, other):
        if self.price<other.price:
            return True
        else: return False
    
    def __le__(self, other):
        if self.price<=other.price:
            return True
        else: return False

    def __gt__(self, other):
        if self.price>other.price:
            return True
        else: return False

    def __ge__(self, other):
        if self.price>=other.price:
            return True
        else: return False