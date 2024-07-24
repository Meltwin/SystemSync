from dataclasses import dataclass, field
from typing import List

from .Project import ProjectConfig
from .YAMLObject import YAMLObject


@YAMLObject(tag="Config")
@dataclass
class YAMLConfiguration:
    version: str
    name: str
    projects: List[ProjectConfig] = field(default_factory=list)

    def __repr__(self) -> str:
        out = f"Configuration {self.name} (v {self.version})"
        for p in self.projects:
            out += f"\n{p}"
        return out
