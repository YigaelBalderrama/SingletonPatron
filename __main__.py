from Disc import Disc
from File import File
from Folder import Folder

def main():
    my_disc = Disc("Yiga")
    my_disc.add_content(Folder("Notas"))
    my_disc.show_actual_capacity()
    my_disc.show_content()
    nota_1=File("Importante")
    nota_1.add_content("Debo acabar los codigos pronto!!!")
    my_disc.add_content(nota_1)
    my_disc.show_content()
    my_disc.show_actual_capacity()
main()