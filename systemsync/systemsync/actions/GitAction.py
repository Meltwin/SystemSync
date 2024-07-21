from ..data import GitTask
from .IAction import IAction

import os

class GitAction(IAction[GitTask]):
    """
    This class takes a GitTask as input and manage it.
    """

    def __int__(self, task: GitTask):
        super().__init__(task)

    def run(self):
        # Check if directory already exist, in this case update it
        if os.path.exists(self._task.dest):
            self._update_repo()
        else:

    def _update_repo(self):
        pass

    def _clone_repo(self):
        pass
