class Triangle:
    def __init__(self,lengths:list,id:int = 1):
        self.__lengths = lengths
        self.__sides = 3
        self.__id_hook = 1
        return None
    def __str__(self):
        return f"Triangle object sides length {self.__sides}"
    __repr__ = __str__
    def __add__(self):
        print("--------------------------INVALID OPERATION------------------------------")
        raise ValueError from None
        return None
    __sub__ = __and__ = __or__ = __xor__ = __mul__ = __mod__ = __divmod__ = __add__
    def __eq__(self,t):
        return self.__lengths == t.__lengths and self.__id_hook == t.__id_hook
    def __ne__(self,t):
        return self.__lengths != t.__lengths or self.__id_hook != t.__id_hook
    __lt__ = __gt__ = __le__ = __ge__ = __add__
