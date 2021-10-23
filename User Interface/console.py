from Logic.crud import create


def show_menu():
    print("1. Deschideti interfata CRUD")
    print("x. Iesire")


def handle_add(cheltuieli):
        id = input('Introduceti id-ul cheltuielii: ')
        numar = input ('Introduceti numarul apartamentului: ')
        suma = input('Introduceti suma chetuielii: ')
        data = input('Introduceti data cheltuielii, in format DD/MM/YYYY: ')
        tip = input('Introduceti tipul cheltuielii (intretinere/canal/alte cheltuieli): ')
        return create(cheltuieli, id, numar, suma, data, tip)



def handle_crud(cheltuieli):
    while True:
        print('1. Adaugare cheltuieli')
        print('2. Modificare cheltuieli')
        print('3. Stergere cheltuieli')
        print('4. Afisare cheltuieli a unui apartament')
        print('r. Revenire')

        optiune = input('Introduceti optiunea: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli)
        elif optiune == 'a':


            


def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Introduceti optiunea: ')
        if optiune == '1':
            handle_crud(cheltuieli)