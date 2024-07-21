from ..data import CmdTask
from .IAction import IAction


class CmdAction(IAction[CmdTask]):
    def __init__(self, task: CmdTask):
        super().__init__(task)
