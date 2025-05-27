# src/domain/common/base_entity.py

from abc import ABC
from uuid import UUID, uuid4
from dataclasses import dataclass, field
from typing import Any


@dataclass(eq=False)
class BaseEntity(ABC):
    """领域实体的基类。"""

    id: UUID

    def __eq__(self, other: Any) -> bool:
        """Entities are equal if their IDs are equal."""
        if not isinstance(other, BaseEntity):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        """Entities are hashed based on their ID."""
        return hash(self.id)
