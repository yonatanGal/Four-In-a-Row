RADIUS=3
DEFAULT_X=''
DEFAULT_Y=''
class Disc:
    def __init__(self,color):
        self.__radius=RADIUS
        self.__color=color
        self.__x_location=DEFAULT_X
        self.__y_location=DEFAULT_Y

    def get_radius(self):
        '''
        :return: the radius of the disc
        '''
        return self.__radius

    def get_color(self):
        '''
        :return: disc color
        '''
        return self.__color

    def get_location(self):
        '''
        :return: disc location as tuple
        '''
        return (self.__x_location,self.__y_location)

    def set_location(self,location):
        '''
        :param location: tuple of x and y locations
        :return: None
        '''
        self.__x_location,self.__y_location=location

    