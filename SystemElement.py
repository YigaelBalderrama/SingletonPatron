from abc import ABC, abstractmethod

class SystemElement(ABC):

    def __init__(self,name):
        self.name = name
        self.weight = 0
        self.content = NotImplementedError

    def properties(self):
        print(f"{self.name}")
        print(f"\t {self.weight}")
    
    @abstractmethod
    def add_content(self,new_content):
        pass
    
    @abstractmethod
    def show_content(self):
        pass