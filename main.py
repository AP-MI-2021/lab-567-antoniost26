from Logic.crud import create
from Tests.test_crud import test_crud
from UserInterface.console import run_ui


def main():
    cheltuieli = []
    cheltuieli = run_ui(cheltuieli)


if __name__=='__main__':
    test_crud()
    main()