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
    
    def _trigger_callbacks(self, event: str, data: Any):
        """
        Trigger all callbacks for an event
        
        Args:
            event: Event name
            data: Event data
            
        Each callback will receive (data, server_info) as arguments
        """
        for callback in self._callbacks.get(event, []):
            try:
                callback(data, self._server_info)
            except Exception as e:
                logger.error(f"Error in {event} callback for server {self._server_info.name}: {str(e)}")

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

class MT5PriceSink(BaseMT5Sink):
    """Sink for price-related events"""
    def OnTick(self, tick) -> None:
        self._trigger_callbacks('tick', tick)

    def OnTickStat(self, tick_stat) -> None:
        self._trigger_callbacks('tick_stat', tick_stat)

class MT5BookSink(BaseMT5Sink):
    """Sink for book-related events"""
    def OnBook(self, book) -> None:
        self._trigger_callbacks('book', book)

    
