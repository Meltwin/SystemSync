from dataclasses import dataclass, field
from typing import List

from .Tasks import ITask
from .YAMLObject import YAMLObject


@YAMLObject(tag="Project")
@dataclass
class ProjectConfig:
    name: str
    tasks: List[ITask] = field(default_factory=list)
