from dataclasses import dataclass, field
from typing import Any, Dict, List

from .Tasks import ITask
from .YAMLObject import YAMLObject


@YAMLObject(tag="Project")
@dataclass
class ProjectConfig:
    name: str
    tasks: List[ITask] = field(default_factory=list)
    vars: Dict[str, Any] = field(default_factory=dict)

    def __repr__(self) -> str:
        out = f"+ Project {self.name}"
        for t in self.tasks:
            out += f"\n\t- {t}"
        return out
