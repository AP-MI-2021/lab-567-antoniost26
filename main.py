from Tests.test_crud import test_crud
from UserInterface.console import run_ui


def main():
    cheltuieli = []  # pentru cheltuieli predefinite folositi get_data() pentru a initializa  variabila cheltuieli;
    cheltuieli = run_ui(cheltuieli)


if __name__ == '__main__':
    test_crud()
    main()
