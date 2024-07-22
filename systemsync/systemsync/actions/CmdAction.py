from ..data import CmdTask
from .IAction import IAction
from ..utils import execute_command


class CmdAction(IAction[CmdTask]):
    """
    Action that just run a simple command in the console.
    """

    def __init__(self, task: CmdTask):
        super().__init__(task)

    def _run(self):
        execute_command(self._task.cmd)
