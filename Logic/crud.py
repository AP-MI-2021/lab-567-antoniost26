from Domain.cheltuieli import creeaza_cheltuiala, get_numar, get_id, get_by_id


def create(lst_cheltuieli, id_cheltuiala, numar_apartament, suma, data, tipul):
    '''
    Creeaza o cheltuiala.
    :param lst_cheltuieli: lista veche de cheltuieli.
    :param id_cheltuiala: id-ul cheltuielii, unic.
    :param numar_apartament: numarul apartamentului, nenul.
    :param suma: suma cheltuielii, nenul.
    :param data: data cheltuielii, nenul.
    :param tipul: tipul cheltuielii, intretinere/canal/alte cheltuieli.
    :return: returneaza o lista in care este adaugata noua cheltuiala.
    '''
    if get_by_id(id, lst_cheltuieli) is not None:
        raise ValueError("Id-ul exista deja.")
    cheltuiala = creeaza_cheltuiala(id_cheltuiala, numar_apartament, suma, data, tipul)
    return lst_cheltuieli + [cheltuiala]

def read(lst_cheltuieli, numar_apartament):
    '''
    Citeste o cheltuiala din "baza de date"
    :param lst_cheltuieli: lista de cheltuieli.
    :param numar_apartament: numarul apartamentului aferent cheltuielii.
    :return: Cheltuiala/cheltuielile cu numarul apartamentului numar_apartament sau lista cu toate cheltuielile, daca numar_apartament = None
    '''
    cheltuiala_cu_nr_ap = []
    for cheltuiala in lst_cheltuieli:
        if get_numar(cheltuiala) == numar_apartament:
            cheltuiala_cu_nr_ap.append(cheltuiala)
    return cheltuiala_cu_nr_ap

def update(lst_cheltuieli, new_cheltuiala):
    '''
    Modifica o cheltuiala anume in functie de numarul de apartament SI id.
    :param lst_cheltuieli: lista cu cheltuieli.
    :param new_cheltuiala: noua cheltuiala, dupa care va fi modificata cea veche.
    :return: lista actualizata cu toate cheltuielile.
    '''
    if get_by_id(get_id(new_cheltuiala), lst_cheltuieli) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat.")
    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_numar(cheltuiala) != get_numar(new_cheltuiala):
            new_cheltuieli.append(cheltuiala)
        elif get_numar(cheltuiala) == get_numar(new_cheltuiala) and get_id(cheltuiala) != get_id(new_cheltuiala):
            new_cheltuieli.append(cheltuiala)
        else:
            new_cheltuieli.append(new_cheltuiala)
    return new_cheltuieli

def delete(lst_cheltuieli, numar_apartament, id):
    '''
    Sterge o cheltuiala a unui apartament.
    :param lst_cheltuieli: lista cu cheltuielile.
    :param numar_apartament: numarul apartamentului a carei cheltuiala va urma sa fie stearsa.
    :return:returneaza lista finala, din care va fi stearsa cheltuiala respectiva.
    '''
    if get_by_id(id, lst_cheltuieli) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat.")
    new_cheltuieli = []
    for cheltuiala in [x for x in lst_cheltuieli if get_numar(x) != numar_apartament]:
        new_cheltuieli.append(cheltuiala)
    for cheltuiala in [x for x in lst_cheltuieli if numar_apartament == get_numar(x) and id != get_id(x)]:
        new_cheltuieli.append(cheltuiala)
    return new_cheltuieli