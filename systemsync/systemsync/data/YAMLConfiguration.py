from dataclasses import dataclass, field
from typing import List

from .Project import ProjectConfig
from .YAMLObject import YAMLObject


@YAMLObject(tag="Config")
@dataclass
class YAMLConfiguration:
    version: str
    projects: List[ProjectConfig] = field(default_factory=list)
