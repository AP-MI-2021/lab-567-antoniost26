import copy

from Domain.cheltuieli import get_id
from Logic.crud import create
from UserInterface.console import undo, redo


def test_undo_redo():
    cheltuieli = []
    undoList = []
    redoList = []
    cheltuieli = create(cheltuieli, 1, 13, 200, '20.02.2002', 'intretinere', undoList, redoList)
    cheltuieli = create(cheltuieli, 2, 14, 220, '20.02.2002', 'intretinere', undoList, redoList)
    cheltuieli = create(cheltuieli, 3, 13, 200, '20.02.2002', 'canal', undoList, redoList)
    cheltuieli = undo(cheltuieli, undoList, redoList)
    assert len(cheltuieli) == 2
    assert get_id(cheltuieli[0]) == 1
    assert get_id(cheltuieli[1]) == 2
    cheltuieli = undo(cheltuieli, undoList, redoList)
    assert len(cheltuieli) == 1
    assert get_id(cheltuieli[0]) == 1
    cheltuieli = undo(cheltuieli, undoList, redoList)
    assert cheltuieli == []
    cheltuieli = undo(cheltuieli, undoList, redoList)
    assert cheltuieli == []
    cheltuieli = create(cheltuieli, 1, 13, 200, '20.02.2002', 'intretinere', undoList, redoList)
    cheltuieli = create(cheltuieli, 2, 14, 220, '20.02.2002', 'intretinere', undoList, redoList)
    cheltuieli = create(cheltuieli, 3, 13, 200, '20.02.2002', 'canal', undoList, redoList)
    cheltuieli_test = cheltuieli
    cheltuieli = redo(cheltuieli, redoList, undoList)
    assert cheltuieli_test == cheltuieli
    cheltuieli = undo(cheltuieli, undoList, redoList)
    assert len(cheltuieli) == 2
    assert get_id(cheltuieli[0]) == 1
    assert get_id(cheltuieli[1]) == 2
    cheltuieli = undo(cheltuieli, undoList, redoList)
    assert len(cheltuieli) == 1
    assert get_id(cheltuieli[0]) == 1
    cheltuieli = create(cheltuieli, 4, 15, 220, '20.02.2002', 'alte cheltuieli', undoList, redoList)
    cheltuieli_test = cheltuieli
    cheltuieli = redo(cheltuieli, redoList, undoList)
    assert cheltuieli_test == cheltuieli
    cheltuieli = undo(cheltuieli, undoList, redoList)
    assert len(cheltuieli) == 1
    assert get_id(cheltuieli[0]) == 1
    cheltuieli = undo(cheltuieli, undoList, redoList)
    assert cheltuieli == []
    cheltuieli = redo(cheltuieli, redoList, undoList)
    assert len(cheltuieli) == 1
    assert get_id(cheltuieli[0]) == 1
    cheltuieli = redo(cheltuieli, redoList, undoList)
    assert len(cheltuieli) == 2
    assert get_id(cheltuieli[0]) == 1
    assert get_id(cheltuieli[1]) == 4
    cheltuieli_test = copy.deepcopy(cheltuieli)
    cheltuieli = redo(cheltuieli, redoList, undoList)
    assert cheltuieli_test == cheltuieli
