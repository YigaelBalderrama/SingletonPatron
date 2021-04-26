from SystemElement import SystemElement

class File(SystemElement):
    
    def __init__(self,name):
        super().__init__(name)
        self.content=""
    
    def __actu_weight(self):
        self.weight=len(self.content)*2

    def add_content(self,new_content):
        SystemElement.add_content(self,new_content)
        self.content +=new_content
        self.__actu_weight()
    
    def show_content(self):
        print(f"File..{self.name}")
            
    