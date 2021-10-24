from Domain.cheltuieli import get_str, creeaza_cheltuiala, get_numar, get_id
from Logic.crud import create, read, update, delete


def show_menu():
    print("1. Deschideti interfata CRUD.")
    print("2. Stergerea tutror cheltuielilor pentru un apartament dat.")
    print("x. Iesire")


def handle_add(cheltuieli):
        id = int(input('Introduceti id-ul cheltuielii: '))
        numar = int(input ('Introduceti numarul apartamentului: '))
        suma = float(input('Introduceti suma chetuielii: '))
        data = str(input('Introduceti data cheltuielii, in format DD.MM.YYYY: '))
        tip = str(input('Introduceti tipul cheltuielii (intretinere/canal/alte cheltuieli): '))
        return create(cheltuieli, id, numar, suma, data, tip)


def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))


def handle_cheltuieli_apartament(cheltuieli, numar_ap):
    cheltuieli_ap = read(cheltuieli, numar_ap)
    for x in cheltuieli_ap:
        print(get_str(x))


def handle_update(cheltuieli):
    id = int(input('Introduceti id-ul cheltuielii: '))
    numar = int(input('Introduceti numarul apartamentului: '))
    suma = float(input('Introduceti suma chetuielii: '))
    data = str(input('Introduceti data cheltuielii, in format DD.MM.YYYY: '))
    tip = str(input('Introduceti tipul cheltuielii (intretinere/canal/alte cheltuieli): '))
    new_cheltuiala = creeaza_cheltuiala(id, numar, suma, data, tip)
    return update(cheltuieli, new_cheltuiala)


def handle_delete(cheltuieli):
    numar_ap = int(input('Dati apartamentul a carei cheltuieli doriti sa o stergeti: '))
    handle_cheltuieli_apartament(cheltuieli, numar_ap)
    id_ap = int(input('Dati id-ul cheltuielii pe care doriti sa o stergeti: '))
    return delete(cheltuieli, numar_ap, id_ap)


def show_crud_menu():
    print('1. Adaugare cheltuieli')
    print('2. Modificare cheltuieli')
    print('3. Stergere cheltuieli')
    print('4. Afisare cheltuieli a unui apartament')
    print('a. Afisare toate cheltuielile')
    print('r. Revenire')


def handle_crud(cheltuieli):
    while True:
        show_crud_menu()
        optiune = input('Introduceti optiunea: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_update(cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_delete(cheltuieli)
        elif optiune == '4':
            numar_ap = input('Dati numarul apartamentului pentru care doriti sa vedeti cheltuielile: ')
            handle_cheltuieli_apartament(cheltuieli, numar_ap)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'r':
            break
        else:
            print('Optiune gresita! Reintroduceti optiunea.')
    return cheltuieli


def handle_delete_for_ap_number(cheltuieli):
    nr_ap = int(input('Introduceti numarul apartamentului pentru care doriti sa stergeti toate cheltuielile: '))
    for cheltuiala in cheltuieli:
        if nr_ap == get_numar(cheltuiala):
            cheltuieli = delete(cheltuieli, get_numar(cheltuiala), get_id(cheltuiala))
    return cheltuieli

def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Dati optiunea: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_delete_for_ap_number(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita! Reintroduceti optiunea.')
    return cheltuieli
