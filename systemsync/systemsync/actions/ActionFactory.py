from ..data.Tasks import *
from .IAction import IAction
from .GitAction import GitAction
from .CmdAction import CmdAction


class ActionFactory:
    @staticmethod
    def action_from_task(task: ITask) -> IAction:
        if isinstance(task, GitTask):
            return GitAction(task)
        elif isinstance(task, CmdTask):
            return CmdAction(task)
