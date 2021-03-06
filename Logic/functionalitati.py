import copy

from Domain.cheltuieli import get_suma, get_tipul, str_to_date, get_date, creeaza_cheltuiala, get_id, get_numar
from Logic.crud import update, delete


def add_value_to_date(suma, data, cheltuieli, undoList, redoList):
    '''
    Adauga o valoare sumei fiecarei cheltuiala.
    :param suma: suma care va fi adaugata cheltuielii.
    :param cheltuieli: lista de cheltuieli.
    :return: returneaza lista de cheluieli dupa ce adauga valoarea.
    '''
    for_pop = 0
    data = str_to_date(data)
    new_cheltuieli = []
    for cheltuiala in cheltuieli:
        if get_date(cheltuiala) == data:
            cheltuieli = update(cheltuieli, creeaza_cheltuiala(
                get_id(cheltuiala),
                get_numar(cheltuiala),
                get_suma(cheltuiala) + suma,
                get_date(cheltuiala),
                get_tipul(cheltuiala),
            ), undoList, redoList)
            for_pop+=1
    for i in range(for_pop-1):
        undoList.pop()
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


def monthly_sum(cheltuieli):
    '''
    Calculeaza suma lunara pentru fiecare apartament.
    :param cheltuieli: lista de cheltuieli.
    :return: un dictionar cu sumele lunare a fiecarui apartament.
    '''
    sum = {}
    for cheltuiala in cheltuieli:
        luna = get_date(cheltuiala).strftime("%m %Y")
        nrAp = get_numar(cheltuiala)
        if luna not in sum:
            sum[luna] = {}
        if nrAp in sum[luna]:
            sum[luna][nrAp] += get_suma(cheltuiala)
        else:
            sum[luna][nrAp] = get_suma(cheltuiala)

    return sum

def sort_for_sum(cheltuieli):
    '''
    Sorteaza lista descrescator in functie de suma.
    :param cheltuieli: lista de cheltuieli.
    :return: lista de cheltuieli sortata.
    '''
    return sorted(cheltuieli, key=get_suma, reverse=True)


def delete_for_ap_number(cheltuieli, nr_ap, undoList, redoList):
    rezultat = copy.deepcopy(cheltuieli)
    for_pop = 0
    for cheltuiala in rezultat:
        if nr_ap == get_numar(cheltuiala):
            rezultat = delete(rezultat, get_numar(cheltuiala), get_id(cheltuiala), undoList, redoList)
            for_pop += 1
    for x in range(for_pop):
        undoList.pop()
    undoList.append(cheltuieli)
    redoList.clear()
    return rezultat