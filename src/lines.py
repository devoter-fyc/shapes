class Line:
    def __init__(self,length:int,pst='A',pend='B'):
        self.__length = length
        self.__points = [pst,pend]
        return None
    def __eq__(self,l):
        return self.__length == l.__length and self.__points == l.__points
    def __ne__