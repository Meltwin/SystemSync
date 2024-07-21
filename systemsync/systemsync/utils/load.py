from ..data import YAMLConfiguration
from .file import read_file
from .errors import PathDontExist

import yaml


def load_configuration(file: str) -> YAMLConfiguration:
    """
    Load a configuration file from the given string

    :param file: the path to the file to load
    :return: a loaded YAML Configuration
    """
    try:
        # Load file
        data = read_file(file)
        if data is None:
            raise PathDontExist(file)

        # Parse YAML Configuration
        config = yaml.safe_load(data)
        return config

    except PathDontExist as e:
        print(f"Error while loading configuration file: \n\t{e}")
