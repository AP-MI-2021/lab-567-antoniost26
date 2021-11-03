from Domain.cheltuieli import get_suma, get_tipul, str_to_date, get_date, creeaza_cheltuiala, get_id, get_numar
from Logic.crud import update


def add_value_to_date(suma, data, cheltuieli):
    '''
    Adauga o valoare sumei fiecarei cheltuiala.
    :param suma: suma care va fi adaugata cheltuielii.
    :param cheltuieli: lista de cheltuieli.
    :return: returneaza lista de cheluieli dupa ce adauga valoarea.
    '''
    data = str_to_date(data)
    new_cheltuieli = []
    for cheltuiala in cheltuieli:
        if get_date(cheltuiala) == data:
            cheltuieli = update(cheltuieli, creeaza_cheltuiala(
                get_id(cheltuiala),
                get_numar(cheltuiala),
                get_suma(cheltuiala) + suma,
                get_date(cheltuiala),
                get_tipul(cheltuiala)
            ))
    return cheltuieli


def max_for_type(cheltuieli):
    '''
    Gaseste maximul sumei pentru fiecare tip de cheltuiala.
    :param cheltuieli: lista de cheltuieli.
    :return: returneaza maximul sumei pentru fiecare tip de cheltuial.
    '''
    rezultat = {}
    for cheltuiala in cheltuieli:
        tip = get_tipul(cheltuiala)
        suma = get_suma(cheltuiala)
        if tip in rezultat:
            if suma > rezultat[tip]:
                rezultat[tip] = suma
        else:
            rezultat[tip] = suma
    return rezultat


def show_monthly_sum(cheltuieli):
    pass




def sort_for_sum(cheltuieli):
    '''
    Sorteaza lista descrescator in functie de suma.
    :param cheltuieli: lista de cheltuieli.
    :return: lista de cheltuieli sortata.
    '''
    return sorted(cheltuieli, key=get_suma, reverse=True)