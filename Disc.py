from SingletonMeta import SingletonMeta
from SystemElement import SystemElement
class Disc(metaclass=SingletonMeta):

    content=[]

    def __init__(self, name_d):
        self.name = name_d
        self.capacity = 0
        self.max_capacity = 256

    def show_content(self):
        for x in range(0, len(self.content)):
            self.content[x].show_content()

    def __actu_weight(self):
        for file in self.content:
            self.capacity+=file.weight
    
    def show_actual_capacity(self):
        print(f"The actual space in disc it's {self.capacity}")

    def __verify_space(self, new_content):
        if self.capacity+new_content.weight>self.max_capacity:
            raise Exception(f"Insufficient disc {self.name} space")
    
    def add_content(self,new_content):
        self.__verify_space(new_content)
        self.content.append(new_content)