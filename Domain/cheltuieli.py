def creeaza_cheltuiala(id_cheltuiala, numar_apartament, suma, data, tipul):
    '''
    Creeaza o cheltuiala.
    :param id_cheltuiala: id-ul cheltuielii, trebuie sa fie unic - int.
    :param numar_apartament: numarul apartamentului, nenul - int.
    :param suma: suma cheltuielii aferente apartamentului, nenul - float.
    :param data: data in care s-a procesat cheltuiala, nenul - string.
    :param tipul: tipul cheltuielii, intretinere/canal/alte cheltuieli - string.
    :return: o cheltuiala.
    '''
    return {
        'id': int(id_cheltuiala),
        'numar': int(numar_apartament),
        'suma': float(suma),
        'data': str(data),
        'tip': str(tipul),
    }


def get_id(cheltuiala):
    '''
    Getter pentru id-ul cheltuielii.
    :param cheltuiala: o cheltuiala de tip dictionar.
    :return: id-ul cheltuielii date ca parametru.
    '''
    return cheltuiala['id']


def get_numar(cheltuiala):
    '''
    Getter pentru numarul apartamentului din cheltuiala.
    :param cheltuiala: o cheltuiala de tip dictionar.
    :return: numarul apartamentului din cheltuiala ca parametru.
    '''
    return cheltuiala['numar']


def get_suma(cheltuiala):
    '''
    Getter pentru suma cheltuielii aferente.
    :param cheltuiala: o cheltuiala de tip dictionar.
    :return: suma cheltuielii aferente ca parametru.
    '''
    return cheltuiala['suma']


def get_date(cheltuiala):
    '''
    Getter pentru data cheltuielii aferente.
    :param cheltuiala:  o cheltuiala de tip dictionar.
    :return: data cheltuielii aferente ca parametru.
    '''
    return cheltuiala['data']


def get_tipul(cheltuiala):
    '''
    Getter pentru tipul celtuielii aferente.
    :param cheltuiala: o cheltuiala de tip dictionar.
    :return: tipul cheltuielii aferente ca parametru.
    '''
    return cheltuiala['tip']


def get_str(cheltuiala):
    return f'Cheltuiala cu id-ul {get_id(cheltuiala)}, pentru numarul apartamentului {get_numar(cheltuiala)}, cu suma de {get_suma(cheltuiala)}, in data de {get_data(cheltuiala)} si de tipul {get_tipul(cheltuiala)}'
