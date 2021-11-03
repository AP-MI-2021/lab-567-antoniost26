from Domain.cheltuieli import creeaza_cheltuiala, get_str, get_by_id
from Logic.crud import create, delete, update


def print_commands():
    print('Adaugare: add [id] [nr apartament] [suma] [data] [tip]')
    print('Stergere: delete [id] [numar apartament]')
    print('Modificare: update [id] [nr apartament] [suma] [data] [tip]')
    print('Afisare: showall')
    print()
    print('Meniu: help')
    print('Iesire din CLI (va iesi in consola veche): exit')
    print('*Nota: mai multe comenzi adaugate pe acelasi rand necesita despartirea prin ";".')


def run_add(params, cheltuieli):
    '''
    Adauga o cheltuiala noua in lista cu cheltuieli.
    :param params: detaliile noii cheltuieli.
    :param cheltuieli: lista cu cheltuieli.
    :return: returneaza lista noua cu cheltuieli.
    '''
    try:
        id = int(params[0])
        numar = int(params[1])
        suma = float(params[2])
        data = str(params[3])
        tip = str(params[4])
        if get_by_id(id, cheltuieli) is not None:
            raise ValueError("Id-ul exista deja.")
        return create(cheltuieli, id, numar, suma, data, tip)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


def run_delete(params, cheltuieli):
    '''
    Sterge o cheltuiala din lista.
    :param params: numarul apartamentului si id-ul cheltuielii, retinute intr-o lista.
    :param cheltuieli: lista cu cheltuielile.
    :return: lista cu cheltuielile dupa stergere.
    '''
    try:
        numar_ap = int(params[1])
        id_ap = int(params[0])
        return delete(cheltuieli, numar_ap, id_ap)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


def run_update(params, cheltuieli):
    '''
    Modifica o cheltuiala existenta.
    :param params: detaliile cheltuielii.
    :param cheltuieli: lista cu cheltuieli.
    :return: lista noua dupa modificare.
    '''
    try:
        id = int(params[0])
        numar = int(params[1])
        suma = float(params[2])
        data = str(params[3])
        tip = str(params[4])
        new_cheltuiala = creeaza_cheltuiala(id, numar, suma, data, tip)
        return update(cheltuieli, new_cheltuiala)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


def run_show_all(cheltuieli):
    '''
    Afiseaza toate cheltuielile.
    :param cheltuieli: lista cu cheltuieli.
    :return: -
    '''
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))


def run_cli(cheltuieli):
    print_commands()

    while True:
        optiuni = input('$ ')
        optiuni = optiuni.split(';')

        try:
            for optiune in optiuni:
                optiune = optiune.split()

                if optiune[0] == 'exit':
                    return cheltuieli
                elif optiune[0] == 'help':
                    print_commands()
                elif optiune[0] == 'showall':
                    run_show_all(cheltuieli)
                elif optiune[0] == 'add':
                    cheltuieli_vechi = cheltuieli[:]
                    cheltuieli = run_add(optiune[1:], cheltuieli)
                    if cheltuieli_vechi != cheltuieli:
                        print("Cheltuiala s-a adaugat cu succes.")
                elif optiune[0] == 'delete':
                    cheltuieli_vechi = cheltuieli[:]
                    cheltuieli = run_delete(optiune[1:], cheltuieli)
                    if cheltuieli_vechi != cheltuieli:
                        print("Cheltuiala a fost stearsa cu succes.")
                elif optiune[0] == 'update':
                    cheltuieli_vechi = cheltuieli[:]
                    cheltuieli = run_update(optiune[1:], cheltuieli)
                    if cheltuieli_vechi != cheltuieli:
                        print("Cheltuiala a fost modificata cu succes.")
                else:
                    print('Optiune gresita! Reintroduceti optiunea.')
        except Exception as error:
            print(f'Eroare: {error}')
