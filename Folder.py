from SystemElement import SystemElement

class Folder(SystemElement):
    
    def __init__(self,name):
        super().__init__(name)
        self.content=[]

    def __actu_weight(self):
        if(len(self.content)>0):
            for filenfolder in self.content:
                self.weight+=filenfolder.weight

    def add_content(self,new_content):
        SystemElement.add_content(self,new_content)
        self.content.append(new_content)
        self.__actu_weight()
    
    def show_content(self):
        print(f"Folder..{self.name}")
        for filenfolder in self.content:
            filenfolder.show_content()
    
