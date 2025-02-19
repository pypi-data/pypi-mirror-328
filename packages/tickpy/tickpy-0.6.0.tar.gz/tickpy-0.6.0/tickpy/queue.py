import heapq
from typing import Callable, Any
from dataclasses import dataclass, field
from tickpy.ticker import _TickerParent

@dataclass(order=True)
class Event:
    run_at: int
    call: Callable[..., None]
    args: tuple[Any] = field(default_factory=tuple)
    kwargs: dict[str, Any] = field(default_factory=dict)

class EventQueue:
    def __init__(self,
                 ticker_ref: _TickerParent):
        self.events: list[Event] = []
        self._ticker_ref = ticker_ref
    
    def schedule(self,
                 event: Event):
        heapq.heappush(self.events, event)
    
    def process_events(self):
        while self.events and self.events[0].run_at <= self._ticker_ref.counter:
            event = heapq.heappop(self.events)
            event.call(*event.args, **event.kwargs)
