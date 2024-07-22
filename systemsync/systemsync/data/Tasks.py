from dataclasses import dataclass, field
from typing import List

from ..utils.logger import Logger, LogSource

from .YAMLObject import YAMLObject


@dataclass
class ITask:
    """
    Task interface
    """

    conditions: List[str] = field(default_factory=list)
    valid: bool = True


@YAMLObject(tag="git")
@dataclass
class GitTask(ITask):
    """
    Task that will interact with a Git repository and sync it
    """

    repo: str = ""
    dest: str = ""
    branch: str | None = None
    dirname: str | None = None

    def __post_init__(self) -> None:
        if self.repo == "":
            Logger.error(LogSource.MAIN, "Git task without a repository URL!")
            self.valid = False
            return

        if self.dest == "":
            Logger.error(LogSource.MAIN, "Git task without a dest URL!")
            self.valid = False
            return


@YAMLObject(tag="cmd")
@dataclass
class CmdTask(ITask):
    """
    Task that will only launch a bash command
    """

    cmd: str = ""
