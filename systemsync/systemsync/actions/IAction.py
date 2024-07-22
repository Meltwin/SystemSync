from abc import abstractmethod
from typing import Generic, TypeVar
from ..data import ITask
from ..utils.errors import UnImplementedMethod


T = TypeVar("T", bound=ITask)


class IAction(Generic[T]):
    """
    Interface for describing the actions
    """

    def __init__(self, task: T):
        self._task = task

    def run(self):
        if self._task.valid:
            self._run()

    @abstractmethod
    def _run(self):
        raise UnImplementedMethod("__run", self.__class__.__name__)
