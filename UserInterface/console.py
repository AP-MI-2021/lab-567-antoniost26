from Domain.cheltuieli import get_str, creeaza_cheltuiala, get_numar, get_id
from Logic.crud import create, read, update, delete
from Logic.functionalitati import add_value_to_all, max_for_type
from UserInterface.cli import run_cli


def show_menu():
    print("1. Deschideti interfata CRUD.")
    print("2. Deschideti interfata CLI.")
    print("3. Stergerea tuturor cheltuielilor pentru un apartament dat.")
    print("4. Adunarea unei valori la toate cheltuielile dintr-o dată citită.")
    print("5. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.")
    print("x. Iesire")


def handle_add(cheltuieli):
    '''
    Adauga o cheltuiala in lista de cheltuieli.
    :param cheltuieli: lista de cheltuieli.
    :return: lista noua de cheltuieli.
    '''
    try:
        id = int(input('Introduceti id-ul cheltuielii: '))
        numar = int(input('Introduceti numarul apartamentului: '))
        suma = float(input('Introduceti suma chetuielii: '))
        data = str(input('Introduceti data cheltuielii, in format DD.MM.YYYY: '))
        tip = str(input('Introduceti tipul cheltuielii (intretinere/canal/alte cheltuieli): '))
        return create(cheltuieli, id, numar, suma, data, tip)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


def handle_show_all(cheltuieli):
    '''
    Afiseaza toate cheltuielile.
    :param cheltuieli: lista de cheltuieli.
    :return: -
    '''
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))


def handle_cheltuieli_apartament(cheltuieli, numar_ap):
    '''
    Afiseaza cheltuielile unui apartament.
    :param cheltuieli: lista cu cheltuieli.
    :param numar_ap: numarul apartamentului a caror cheltuieli vor fi afisate.
    :return: -
    '''
    cheltuieli_ap = read(cheltuieli, numar_ap)
    for x in cheltuieli_ap:
        print(get_str(x))


def handle_update(cheltuieli):
    '''
    Modifica o cheltuiala.
    :param cheltuieli: lista de cheltuieli.
    :return: lista de cheltuieli dupa ce a fost modificata.
    '''
    try:
        id = int(input('Introduceti id-ul cheltuielii: '))
        numar = int(input('Introduceti numarul apartamentului: '))
        suma = float(input('Introduceti suma chetuielii: '))
        data = str(input('Introduceti data cheltuielii, in format DD.MM.YYYY: '))
        tip = str(input('Introduceti tipul cheltuielii (intretinere/canal/alte cheltuieli): '))
        new_cheltuiala = creeaza_cheltuiala(id, numar, suma, data, tip)
        return update(cheltuieli, new_cheltuiala)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


def handle_delete(cheltuieli):
    '''
    Sterge o cheltuiala dupa numarul de apartament si id.
    :param cheltuieli: lista cu cheltuieli.
    :return: lista cu cheltuieli dupa stergerea cheltuielii.
    '''
    try:
        numar_ap = int(input('Dati apartamentul a carei cheltuieli doriti sa o stergeti: '))
        handle_cheltuieli_apartament(cheltuieli, numar_ap)
        id_ap = int(input('Dati id-ul cheltuielii pe care doriti sa o stergeti: '))
        return delete(cheltuieli, numar_ap, id_ap)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


def handle_delete_for_ap_number(cheltuieli):
    '''
    Sterge toate cheltuielile pentru un apartament anume.
    :param cheltuieli: lista de cheltuieli.
    :return: lista noua de cheltuieli, dupa ce au fost sterse toate.
    '''
    try:
        nr_ap = int(input('Introduceti numarul apartamentului pentru care doriti sa stergeti toate cheltuielile: '))
        for cheltuiala in cheltuieli:
            if nr_ap == get_numar(cheltuiala):
                cheltuieli = delete(cheltuieli, get_numar(cheltuiala), get_id(cheltuiala))
        return cheltuieli
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


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
            try:
                numar_ap = input('Dati numarul apartamentului pentru care doriti sa vedeti cheltuielile: ')
                handle_cheltuieli_apartament(cheltuieli, numar_ap)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
                return cheltuieli
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'r':
            break
        else:
            print('Optiune gresita! Reintroduceti optiunea.')
    return cheltuieli


def handle_add_value_to_all(cheltuieli):
    '''
    Adauga o valoare tuturor cheltuielilor
    :param cheltuieli: lista de cheltuieli existenta deja.
    :return: returneaza lista cu noile sume ale cheltuielilor.
    '''
    try:
        suma = float(input("Dati suma pe care doriti sa o adaugati la cheltuieli: "))
        return add_value_to_all(suma, cheltuieli)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


def handle_max_for_type(cheltuieli):
    '''
    Gestioneaza functia de gasire a maximului pentru fiecare tip de cheltuiala.
    :param cheltuieli: lista de cheltuieli.
    :return: o lista de maxime pentru fiecare tip de cheluiala, fara a modifica lista de cheltuieli.
    '''
    rezultat = max_for_type(cheltuieli)
    for tip in rezultat:
        print("Pentru cheltuiala de tip {} suma maxima este: {} lei.".format(tip, rezultat[tip]))


def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Dati optiunea: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli)
        elif optiune == '2':
            cheltuieli = run_cli(cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_delete_for_ap_number(cheltuieli)
        elif optiune == '4':
            cheltuieli = handle_add_value_to_all(cheltuieli)
        elif optiune == '5':
            handle_max_for_type(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita! Reintroduceti optiunea.')
    return cheltuieli
