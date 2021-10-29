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
    return [
        int(id_cheltuiala),
        int(numar_apartament),
        float(suma),
        str(data),
        str(tipul),
    ]


#'id':
#'numar:
#'suma':
#'data':
#'tip':


def get_id(cheltuiala):
    '''
    Getter pentru id-ul cheltuielii.
    :param cheltuiala: o cheltuiala de tip dictionar.
    :return: id-ul cheltuielii date ca parametru.
    '''
    return cheltuiala[0]

def get_by_id(id, cheltuieli):
    '''
    Functie folosita pentru exceptie, in care id-ul deja se afla in cheltuieli.
    :param id: id-ul chetluielii.
    :param cheltuieli: lista de cheltuieli.
    :return: returneaza cheltuiala cu id-ul dat.
    '''
    for cheltuiala in cheltuieli:
        if get_id(cheltuiala) == id:
            return cheltuiala

def get_numar(cheltuiala):
    '''
    Getter pentru numarul apartamentului din cheltuiala.
    :param cheltuiala: o cheltuiala de tip dictionar.
    :return: numarul apartamentului din cheltuiala ca parametru.
    '''
    return cheltuiala[1]


def get_suma(cheltuiala):
    '''
    Getter pentru suma cheltuielii aferente.
    :param cheltuiala: o cheltuiala de tip dictionar.
    :return: suma cheltuielii aferente ca parametru.
    '''
    return cheltuiala[2]


def get_date(cheltuiala):
    '''
    Getter pentru data cheltuielii aferente.
    :param cheltuiala:  o cheltuiala de tip dictionar.
    :return: data cheltuielii aferente ca parametru.
    '''
    return cheltuiala[3]


def get_tipul(cheltuiala):
    '''
    Getter pentru tipul celtuielii aferente.
    :param cheltuiala: o cheltuiala de tip dictionar.
    :return: tipul cheltuielii aferente ca parametru.
    '''
    return cheltuiala[4]


def get_str(cheltuiala):
    return f'Cheltuiala cu id-ul {get_id(cheltuiala)}, pentru numarul apartamentului {get_numar(cheltuiala)}, cu suma de {get_suma(cheltuiala)} lei, in data de {get_date(cheltuiala)} si de tipul {get_tipul(cheltuiala)}'
