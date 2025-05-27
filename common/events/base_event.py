# src/domain/common/events/base_event.py

from abc import ABC
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime, timezone


@dataclass(frozen=True)
class DomainEvent(ABC):
    """领域事件的基类。"""

    event_id: UUID = field(default_factory=uuid4, init=False)
    occurred_on: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc), init=False
    )
