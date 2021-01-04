""" Core module """
from io import StringIO

from odbinfo.writer import write_dict


def main():
    """ entry point """
    persons = {"Hilbert": 50, "Bach": 67}
    out = StringIO()
    write_dict(persons, out)
    print(out.getvalue())


if __name__ == '__main__':
    main()
