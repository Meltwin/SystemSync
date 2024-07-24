from os import path

from .errors import PathDontExist


def read_file(f: str) -> str | None:
    """
    Open the given file and read its content. If the file doesn't exist throw an

    :param f:
    :return:
    """
    if not path.exists(f):
        raise PathDontExist(f)

    data = None
    with open(f, "r") as data_file:
        data = data_file.read()
    return data
