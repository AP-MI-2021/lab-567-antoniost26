from Tests.test_crud import all_tests

from UserInterface.console import run_ui


def main():
    cheltuieli = []
    cheltuieli = run_ui(cheltuieli)


if __name__ == '__main__':
    all_tests()
    main()
