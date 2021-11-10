from Tests.test_crud import all_tests, get_data

from UserInterface.console import run_ui


def main():
    cheltuieli = get_data()
    cheltuieli = run_ui(cheltuieli)


if __name__ == '__main__':
    all_tests()
    main()
