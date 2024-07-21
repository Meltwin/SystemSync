from typing import Generic, TypeVar
from ..data import ITask
from ..utils.errors import UnImplementedMethod


T = TypeVar("T")


class IAction(Generic[T]):
    """
    Interface for describing the actions
    """

    def __init__(self, task: T):
        self._task = task

    def run(self):
        raise UnImplementedMethod("run", self.__class__.__name__)
