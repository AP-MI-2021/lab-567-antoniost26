from Domain.cheltuieli import creeaza_cheltuiala, get_numar, get_id
from Logic.crud import create, read, update, delete
from Logic.functionalitati import add_value_to_date, max_for_type, sort_for_sum
from Tests.test_undo_redo import test_undo_redo


def get_data():
    return [
        creeaza_cheltuiala(1, 99, 202, '13.05.2002', 'intretinere'),
        creeaza_cheltuiala(2, 99, 200, '25.05.2002', 'alte cheltuieli'),
        creeaza_cheltuiala(3, 92, 200, '13.05.2002', 'intretinere'),
        creeaza_cheltuiala(4, 95, 200, '13.05.2002', 'intretinere'),
        creeaza_cheltuiala(5, 95, 220, '24.05.2002', 'canal'),
        creeaza_cheltuiala(6, 93, 200, '13.05.2002', 'intretinere'),
        creeaza_cheltuiala(7, 93, 200, '24.05.2002', 'alte cheltuieli'),
    ]


def test_create():
    cheltuieli = get_data()
    undoList = []
    redoList = []
    params = (8, 93, 200, '25.05.2002', 'canal')
    new_cheltuiala = creeaza_cheltuiala(*params)
    new_cheltuieli = create(cheltuieli, *params, undoList, redoList)

    assert len(new_cheltuieli) == len(cheltuieli) + 1

    # found = False
    # for cheltuiala in new_cheltuieli:
    #    if cheltuiala == new_cheltuiala:
    #        found = True
    assert new_cheltuiala in new_cheltuieli


def test_read():
    cheltuieli = get_data()
    some_c = cheltuieli[2]
    testread = read(cheltuieli, get_numar(some_c))
    for x in range(len(testread) - 1):
        assert get_numar(testread(x)) == get_numar(some_c)


def test_update():
    cheltuieli = get_data()
    c_updated = creeaza_cheltuiala(1, 99, 230, '13.05.2002', 'intretinere')
    updated = update(cheltuieli, c_updated, undoList=[], redoList=[])
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
    deleted = delete(cheltuieli, to_delete_ap, to_delete_id, undoList=[], redoList=[])
    assert c_deleted not in deleted
    assert c_deleted in cheltuieli
    assert len(deleted) == len(cheltuieli) - 1


def test_add_value_to_date():
    cheltuieli = get_data()
    to_add = 100
    data = '22.02.2002'
    old_list = cheltuieli
    add_value_to_date(to_add, data, cheltuieli)
    assert len(old_list) == len(cheltuieli)


def test_max_for_type():
    cheltuieli = get_data()
    rezultat = max_for_type(cheltuieli)
    assert len(rezultat) == 3
    assert rezultat['intretinere'] == 202.00
    assert rezultat['alte cheltuieli'] == 200.00
    assert rezultat['canal'] == 220.00


def test_sort_for_sum():
    cheltuieli = get_data()
    rezultat = sort_for_sum(cheltuieli)
    assert get_id(rezultat[0]) == 5
    assert get_id(rezultat[1]) == 1
    assert get_id(rezultat[2]) == 2
    assert get_id(rezultat[3]) == 3
    assert get_id(rezultat[4]) == 4
    assert get_id(rezultat[5]) == 6
    assert get_id(rezultat[6]) == 7


def test_crud():
    test_read()
    test_create()
    test_update()
    test_delete()
    test_add_value_to_date()
    test_max_for_type()
    test_sort_for_sum()
    test_undo_redo()
