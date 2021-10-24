from Domain.cheltuieli import creeaza_cheltuiala, get_numar, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        creeaza_cheltuiala(1, 99, 200, '13.05.2002', 'intretinere'),
        creeaza_cheltuiala(2, 99, 200, '25.05.2002', 'alte cheltuieli'),
        creeaza_cheltuiala(3, 92, 200, '13.05.2002', 'intretinere'),
        creeaza_cheltuiala(4, 95, 200, '13.05.2002', 'intretinere'),
        creeaza_cheltuiala(5, 95, 200, '24.05.2002', 'canal'),
        creeaza_cheltuiala(6, 93, 200, '13.05.2002', 'intretinere'),
        creeaza_cheltuiala(7, 93, 200, '24.05.2002', 'alte cheltuieli'),
    ]

def test_create():
    cheltuieli = get_data()
    params = (8, 93, 200, '25.05.2002', 'canal')
    new_cheltuiala = creeaza_cheltuiala(*params)
    new_cheltuieli = create(cheltuieli, *params)

    assert len(new_cheltuieli) == len(cheltuieli) + 1

    #found = False
    #for cheltuiala in new_cheltuieli:
    #    if cheltuiala == new_cheltuiala:
    #        found = True
    assert new_cheltuiala in new_cheltuieli

def test_read():
    cheltuieli = get_data()
    some_c = cheltuieli[2]
    testread = read(cheltuieli, get_numar(some_c))
    for x in range(len(testread)-1):
        assert get_numar(testread(x)) == get_numar(some_c)

def test_update():
    cheltuieli = get_data()
    c_updated = creeaza_cheltuiala(1, 99, 230, '13.05.2002', 'intretinere')
    updated = update(cheltuieli, c_updated)
    assert c_updated in updated
    assert c_updated not in cheltuieli
    assert len(updated) == len(cheltuieli)

def test_delete():
    cheltuieli = get_data()
    to_delete_ap = 99
    to_delete_id = 1
    c_deleted = None
    for c in [x for x in cheltuieli if to_delete_ap == get_numar(x) and to_delete_id == get_id(x)]:
        c_deleted = c
    deleted = delete(cheltuieli, to_delete_ap, to_delete_id)
    assert c_deleted not in deleted
    assert c_deleted in cheltuieli
    assert len(deleted) == len(cheltuieli) - 1


def test_crud():
    test_read()
    test_create()
    test_update()
    test_delete()