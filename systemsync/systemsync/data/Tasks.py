from dataclasses import dataclass

from .YAMLObject import YAMLObject


class ITask:
    """
    Task interface
    """
    pass


@YAMLObject(tag="git")
@dataclass
class GitTask(ITask):
    """
    Task that will interact with a Git repository and sync it
    """
    repo: str


@YAMLObject(tag="cmd")
@dataclass
class CmdTask(ITask):
    """
    Task that will only launch a bash command
    """
    cmd: str
