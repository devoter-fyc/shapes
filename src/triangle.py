class Triangle:
    def __init__(self,lengths:list):
        self.__lengths = lengths
        self.__sides = 3
        return None
    def __str__(self):
        return f"Triangle object sides length {self.__sides}"
    __repr__ = __str__
    def __add__(self):
        print("--------------------------INVALID OPERATION------------------------------")
        raise ValueError from None
        return None
    __s
