from abc import abstractmethod
from typing import Any, Dict, Generic, List, TypeVar
import re
from ..data import ITask
from ..utils.errors import UnImplementedMethod


T = TypeVar("T", bound=ITask)


class IAction(Generic[T]):
    """
    Interface for describing the actions
    """

    other_primitives = [bool, int, float]

    def __init__(self, task: T, vars: Dict[str, Any]):
        self._task = task

        if self._task.valid:
            self.__replace_vars_in_props(vars)

    def run(self) -> bool:
        """
        Run the action based on the task configuration.
        """
        if not self._task.valid:
            return False

        # Run task

        if not self.__test_conditions():
            return False
        self._run()
        return True

    @abstractmethod
    def _run(self) -> None:
        raise UnImplementedMethod("__run", self.__class__.__name__)

    def __test_conditions(self) -> bool:
        """
        Evaluate the conditions to see whether we should run the task or not.
        """
        runnable = True
        index = 0
        n_cond = len(self._task.conditions)
        while index < n_cond and runnable:
            runnable = runnable and bool(eval(self._task.conditions[index]))
            index += 1
        return runnable

    def __replace_vars_in_props(self, vars: Dict[str, Any]) -> None:
        """
        Replace all var instances inside of the string of the conditions and members of the task.
        Look for patterns ${varname}

        Args:
            vars (Dict[str, Any]): the vars values to be integrated
        """

        def replace_in_str(s: str) -> str:
            # Find var instances
            matchs = re.findall("\\$\\{([a-zA-Z0-9]+)\\}", s)

            # Replace vars instances
            for m in matchs:
                if m not in vars.keys():
                    continue
                s = s.replace(f'{r"${"}{m}{r"}"}', vars[m])
            return s

        def replace_in_array(arr: List) -> List:
            for i in range(len(arr)):
                if arr[i] is None:
                    continue
                elif type(arr[i]) is str:
                    arr[i] = replace_in_str(arr[i])
                elif type(arr[i]) is list:
                    arr[i] = replace_in_array(arr[i])
                elif type(arr[i]) is dict:
                    arr[i] = replace_in_dict(arr[i])
                elif type(arr[i]) not in IAction.other_primitives:
                    arr[i] = replace_in_obj(arr[i])
            return arr

        def replace_in_dict(d: Dict) -> Dict:
            for i in d.keys():
                if d[i] is None:
                    continue
                elif type(d[i]) is str:
                    d[i] = replace_in_str(d[i])
                elif type(d[i]) is list:
                    d[i] = replace_in_array(d[i])
                elif type(d[i]) is dict:
                    d[i] = replace_in_dict(d[i])
                elif type(d[i]) not in IAction.other_primitives:
                    d[i] = replace_in_obj(d[i])
            return d

        def replace_in_obj(o: object):
            for att_name, att_val in o.__dict__.items():
                if att_val is None:
                    continue
                elif type(att_val) is str:
                    o.__setattr__(att_name, replace_in_str(att_val))
                elif type(att_val) is list:
                    o.__setattr__(att_name, replace_in_array(att_val))
                elif type(att_val) is dict:
                    o.__setattr__(att_name, replace_in_dict(att_val))
                elif type(att_val) not in IAction.other_primitives:
                    o.__setattr__(att_name, replace_in_obj(att_val))
            return o

        # Iterate over all attributes of the instance and look for strings
        replace_in_obj(self._task)
