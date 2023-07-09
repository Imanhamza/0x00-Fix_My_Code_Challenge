#!/usr/bin/python3
'''
Square module to deal with 4 sided rectangle
'''


class Square():
    '''
    Calss Square
    public attribute hight(int): the hight of the rectengle
    public attribute width(int): the width of the rectengle
    '''
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        ''' Initiation of the class '''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def Permiter_of_my_square(self):
        ''' Permiter Of My Square '''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        ''' Printable representation of the Square '''
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    ''' Create an object '''
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.Permiter_of_my_square())
