from typing import Callable, Dict, Any, Optional, NamedTuple
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass
class ServerInfo:
    """Server information passed to callbacks"""
    id: int
    name: str
    type: str  # 'demo' or 'live'

class MTEvent:
    """
    Event object that encapsulates all event-related data.

    Attributes:
        type (str): The type of event (e.g., 'tick', 'book', 'tick_stat')
        data (tuple): Tuple containing the event data arguments
        server_info (ServerInfo): Information about the MT5 server
    """
    def __init__(self, event_type: str, data: tuple, server_info) -> None:
        """
        Initialize a new MT5 event.

        Args:
            event_type (str): The type of event
            data (tuple): Tuple containing the event data arguments
            server_info: Server information object
        """
        self.type = event_type
        self.data = data
        self.server_info = server_info

    def __str__(self) -> str:
        """Return a string representation of the event."""
        return f"MTEvent(type={self.type}, data={self.data}, server={self.server_info.name})"


class BaseMT5Sink:
    """Base class for MT5 event sinks"""
    def __init__(self, server_info: ServerInfo):
        self._callbacks: Dict[str, list[Callable]] = {}
        self._server_info = server_info
    
    def add_callback(self, event: str, callback: Callable):
        """Add callback for specific event"""
        if event not in self._callbacks:
            self._callbacks[event] = []
        self._callbacks[event].append(callback)
    
    def _trigger_callbacks(self, event: str, *args):
        """
        Trigger all callbacks registered for an event with a structured event object.
        
        This method creates an MTEvent object that encapsulates all event-related data
        and passes it to each callback. This provides a more structured approach to
        event handling and ensures consistent data access patterns.

        Args:
            event (str): Event name/type (e.g., 'tick', 'book', 'tick_stat')
            *args: Variable positional arguments containing the event data

        Example:
            For a tick event, the callback would receive:
            callback(MTEvent(
                type='tick',
                data=(symbol, tick),
                server_info=self._server_info
            ))
        """
        event_data = MTEvent(event, args, self._server_info)
        for callback in self._callbacks.get(event, []):
            try:
                callback(event_data)
            except Exception as e:
                logger.error(
                    f"Error in {event} callback for server {self._server_info.name}: {str(e)}"
                )
class MT5UserSink(BaseMT5Sink):
    """Sink for user-related events"""
    def OnUserAdd(self, user) -> None:
        self._trigger_callbacks('user_add', user)
        
    def OnUserUpdate(self, user) -> None:
        self._trigger_callbacks('user_update', user)

    def OnUserDelete(self, user) -> None:
        self._trigger_callbacks('user_delete', user)
        
    def OnUserLogin(self, user) -> None:
        self._trigger_callbacks('user_login', user)
    
    def OnUserLogout(self, user) -> None:
        self._trigger_callbacks('user_logout', user)

    def OnUserArchive(self, user) -> None:
        self._trigger_callbacks('user_archive', user)

    def OnUserRestore(self, user) -> None:
        self._trigger_callbacks('user_restore', user)

class MT5DealSink(BaseMT5Sink):
    """Sink for deal-related events"""
    def OnDealAdd(self, deal) -> None:
        self._trigger_callbacks('deal_add', deal)
    
    def OnDealUpdate(self, deal) -> None:
        self._trigger_callbacks('deal_update', deal)
    
    def OnDealDelete(self, deal) -> None:
        self._trigger_callbacks('deal_delete', deal)

class MT5PositionSink(BaseMT5Sink):
    """Sink for position-related events"""
    def OnPositionAdd(self, position) -> None:
        self._trigger_callbacks('position_add', position)
    
    def OnPositionUpdate(self, position) -> None:
        self._trigger_callbacks('position_update', position)
    
    def OnPositionDelete(self, position) -> None:
        self._trigger_callbacks('position_delete', position)

class MT5OrderSink(BaseMT5Sink):
    """Sink for order-related events"""
    def OnOrderAdd(self, order) -> None:
        self._trigger_callbacks('order_add', order)
    
    def OnOrderUpdate(self, order) -> None:
        self._trigger_callbacks('order_update', order)
    
    def OnOrderDelete(self, order) -> None:
        self._trigger_callbacks('order_delete', order)

class MT5SummarySink(BaseMT5Sink):
    """Sink for summary-related events"""
    def OnSummaryUpdate(self, summary) -> None:
        self._trigger_callbacks('summary_update', summary)

class MT5TickSink(BaseMT5Sink):
    """Sink for tick-related events"""
    def OnTick(self, symbol, tick) -> None:
        self._trigger_callbacks('tick', symbol, tick)

    def OnTickStat(self, tick_stat) -> None:
        self._trigger_callbacks('tick_stat', tick_stat)

class MT5BookSink(BaseMT5Sink):
    """Sink for book-related events"""
    def OnBook(self, symbol, book) -> None:
        self._trigger_callbacks('book', symbol, book)

    
