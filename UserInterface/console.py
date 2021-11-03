import copy

from Domain.cheltuieli import get_str, creeaza_cheltuiala, get_numar, get_id, get_by_id, get_suma, get_date, get_tipul
from Logic.crud import create, read, update, delete
from Logic.functionalitati import max_for_type, add_value_to_date, sort_for_sum
from UserInterface.cli import run_cli


def show_menu():
    print("1. Deschideti interfata CRUD.")
    print("2. Deschideti interfata CLI.")
    print("x. Iesire")


def handle_add(cheltuieli, undoList, redoList):
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
        rezultat = create(cheltuieli, id, numar, suma, data, tip)
        undoList.append(cheltuieli)
        redoList.clear()
        return rezultat
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


def handle_update(cheltuieli, undoList, redoList):
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
        rezultat = update(cheltuieli, new_cheltuiala)
        undoList.append(cheltuieli)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


def handle_delete(cheltuieli, undoList, redoList):
    '''
    Sterge o cheltuiala dupa numarul de apartament si id.
    :param cheltuieli: lista cu cheltuieli.
    :return: lista cu cheltuieli dupa stergerea cheltuielii.
    '''
    try:
        numar_ap = int(input('Dati apartamentul a carei cheltuieli doriti sa o stergeti: '))
        handle_cheltuieli_apartament(cheltuieli, numar_ap)
        id_ap = int(input('Dati id-ul cheltuielii pe care doriti sa o stergeti: '))
        rezultat = delete(cheltuieli, numar_ap, id_ap)
        undoList.append(cheltuieli)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


def handle_delete_for_ap_number(cheltuieli, undoList, redoList):
    '''
    Sterge toate cheltuielile pentru un apartament anume.
    :param cheltuieli: lista de cheltuieli.
    :return: lista noua de cheltuieli, dupa ce au fost sterse toate.
    '''
    try:
        nr_ap = int(input('Introduceti numarul apartamentului pentru care doriti sa stergeti toate cheltuielile: '))
        rezultat = copy.deepcopy(cheltuieli)
        for cheltuiala in rezultat:
            if nr_ap == get_numar(cheltuiala):
                rezultat = delete(rezultat, get_numar(cheltuiala), get_id(cheltuiala))
        undoList.append(cheltuieli)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


def show_crud_menu():
    print('1. Adaugare cheltuieli')
    print('2. Modificare cheltuieli')
    print('3. Stergere cheltuieli')
    print('4. Afisare cheltuieli a unui apartament')
    print("5. Stergerea tuturor cheltuielilor pentru un apartament dat.")
    print("6. Adunarea unei valori la toate cheltuielile dintr-o dată citită.")
    print("7. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.")
    print("8. Ordonarea cheltuielilor descrescător după sumă.")
    print("u. Undo.")
    print("r. Redo.")
    print('a. Afisare toate cheltuielile')
    print('x. Revenire')





def handle_add_value_to_date(cheltuieli, undoList, redoList):
    '''
    Adauga o valoare tuturor cheltuielilor
    :param cheltuieli: lista de cheltuieli existenta deja.
    :return: returneaza lista cu noile sume ale cheltuielilor.
    '''
    try:
        suma = float(input("Dati suma pe care doriti sa o adaugati la cheltuieli: "))
        data = input("Dati data pentru care doriti sa adaugati:")
        rezultat = add_value_to_date(suma, data, cheltuieli)
        undoList.append(cheltuieli)
        redoList.clear()
        return rezultat
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


def handle_sort_for_sum(cheltuieli):
    handle_show_all(sort_for_sum(cheltuieli))

def handle_crud(cheltuieli):
    undoList = []
    redoList = []
    while True:
        show_crud_menu()

        optiune = input('Introduceti optiunea: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli, undoList, redoList)
        elif optiune == '2':
            cheltuieli = handle_update(cheltuieli, undoList, redoList)
        elif optiune == '3':
            cheltuieli = handle_delete(cheltuieli, undoList, redoList)
        elif optiune == '4':
            try:
                numar_ap = input('Dati numarul apartamentului pentru care doriti sa vedeti cheltuielile: ')
                handle_cheltuieli_apartament(cheltuieli, numar_ap)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
                return cheltuieli
        elif optiune == '5':
            cheltuieli = handle_delete_for_ap_number(cheltuieli, undoList, redoList)
        elif optiune == '6':
            cheltuieli = handle_add_value_to_date(cheltuieli, undoList, redoList)
        elif optiune == '7':
            handle_max_for_type(cheltuieli)
        elif optiune == '8':
            handle_sort_for_sum(cheltuieli)
        elif optiune == 'u':
            if len(undoList) > 0:
                redoList.append(cheltuieli)
                cheltuieli = undoList.pop()
            else:
                print('Nu se poate face undo.')
        elif optiune == 'r':
            if len(redoList) > 0:
                undoList.append(cheltuieli)
                cheltuieli = redoList.pop()
            else:
                print('Nu se poate face redo.')
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita! Reintroduceti optiunea.')
    return cheltuieli


def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Dati optiunea: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli)
        elif optiune == '2':
            cheltuieli = run_cli(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita! Reintroduceti optiunea.')
    return cheltuieli
