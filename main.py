from Tests.test_crud import test_crud, get_data
from UserInterface.console import run_ui


def main():
    cheltuieli = get_data()
    cheltuieli = run_ui(cheltuieli)


if __name__=='__main__':
    test_crud()
    main()