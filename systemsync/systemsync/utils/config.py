from enum import Enum
from typing import Any, Dict

from ..data import YAMLConfiguration, ProjectConfig
from .file import read_file
from .errors import PathDontExist
from . import execute_command

import yaml


def load_configuration(file: str) -> YAMLConfiguration:
    """
    Load a configuration file from the given string

    Args:
        - file: the path to the file to load

    Returns: a loaded YAML Configuration
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
    return YAMLConfiguration("0.0.0", "Unknown")


class RunType(Enum):
    CONSTANT = "C"
    PYTHON = "P"
    SHELL = "S"


def compute_vars(project: ProjectConfig) -> Dict[str, Any]:
    """
    Load the several vars from a project

    Args:
        -project (ProjectConfig): the project description

    Returns:
        Dict[str, Any]: a map of the var key and its values
    """
    out = {}
    for v, cmd in project.vars.items():
        current_cmd = cmd
        run_type = RunType.CONSTANT

        # Check if there's a prefix for the language to use
        if len(cmd) > 1 and cmd[1] == "/":
            run_type = RunType(cmd[:1])
            current_cmd = cmd[2:]

        # Execute command
        match run_type:
            case RunType.CONSTANT:
                out[v] = current_cmd
            case RunType.PYTHON:
                out[v] = eval(current_cmd)
            case RunType.SHELL:
                stdout, _ = execute_command(current_cmd)
                out[v] = stdout
    return out
