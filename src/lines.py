class Line:
    def __init__(self,length:int,pst='A',pend='B'):
        self.__length = length
        self.__points = [pst,pend]
        return None
    def __eq__(self,l):
        return self.__length == l.__length and self.__points == l.__points
    def __ne__(self,l):
        return self.__length != l.__length or self.__points != l.__points
    def __lt__(self,l):
        return self.__length < l.__length
    def __gt__(self,l):
        return self.__length > l.__length
    def __le__(self,l):
        return self.__length <= l.__length
    def __ge__(self,l):
        return self.__length >= l.__length
    def __add__(self,v):
        self.__length += v
        return None
    def __sub__(self,v):
        self.__length -= v
        return None
    def __int__(self):
        return int(self.__length)
    def __float__(self):
        return float(self.__length)
    def __mul__(self):
        raise ValueError("Invalid operation")
        return None
    __mod__ = __mul__
    __divmod__ = __mul__
    __and__ = __mul__
    __or__ = __mul__
    __xor__ = __mul__
    __neg__ = __mul__
    def __abs__(self):
        return self.__length
    def __str__(self):
        return f"Line object at {self.__points} length {self.__length}"
    __repr__ = __str__
    def __index__(self):
        return self.__length
    def __call__(self):
        print(self.__str__())
        return 0
    
