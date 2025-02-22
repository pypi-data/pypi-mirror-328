from dataclasses import dataclass

from aisle.analyser.entities.links import Link
from aisle.analyser.entities.project import ProjectEntity


@dataclass
class ActorEntity(ProjectEntity):
    """Actor entity."""

    name: str
    description: str
    links: list[Link]
    tags: list[str]


@dataclass
class SystemEntity(ProjectEntity):
    """System entity."""

    name: str
    description: str
    links: list[Link]
    tags: list[str]
    is_external: bool = False
