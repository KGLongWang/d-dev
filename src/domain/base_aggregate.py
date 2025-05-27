# src/domain/common/base_aggregate.py

from abc import ABC
from dataclasses import field, dataclass
from typing import List, Any
from src.domain.common.base_entity import BaseEntity
import logging


@dataclass(eq=False)
class BaseAggregateRoot(BaseEntity, ABC):
    """聚合根的基类。"""

    _domain_events: List[Any] = field(default_factory=list, init=False, repr=False)
    logger: logging.Logger = field(
        default=logging.getLogger(__name__), init=False, repr=False
    )

    def add_domain_event(self, event: Any):
        """将领域事件添加到内部列表。"""
        self.logger.debug(
            f"Aggregate {self.__class__.__name__} (ID: {self.id}) adding event: {type(event).__name__}"
        )
        self._domain_events.append(event)

    def clear_domain_events(self):
        """清除内部列表中的所有领域事件。"""
        self.logger.debug(
            f"Aggregate {self.__class__.__name__} (ID: {self.id}) clearing events."
        )
        self._domain_events.clear()

    @property
    def domain_events(self) -> List[Any]:
        """返回内部领域事件列表的副本。"""
        return self._domain_events[:]
