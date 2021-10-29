from Domain.cheltuieli import get_suma, get_tipul


def add_value_to_all(suma, cheltuieli):
    '''
    Adauga o valoare sumei fiecarei cheltuiala.
    :param suma: suma care va fi adaugata cheltuielii.
    :param cheltuieli: lista de cheltuieli.
    :return: returneaza lista de cheluieli dupa ce adauga valoarea.
    '''
    new_cheltuieli = []
    for cheltuiala in cheltuieli:
        cheltuiala['suma'] += suma
        new_cheltuieli.append(cheltuiala)
    return new_cheltuieli


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