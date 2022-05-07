class Ciclista:
    def _init_(self):
        self.__name=None
        self.__age=None
        self.__country=None
        self.__team=None
        self.__time=None
    
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def country(self):
        return self.__country

    @property
    def team(self):
        return self.__team

    @property
    def time(self):
        return self.__time
    

    @name.setter
    def name(self,nombre):
        self.__name=nombre

    @age.setter
    def age(self,edad):
        self.__age=edad

    @country.setter
    def country(self,pais):
        self.__country=pais

    @team.setter
    def team(self,equipo):
        self.__team=equipo

    @time.setter
    def time(self,tiempo):
        self.__time=tiempo