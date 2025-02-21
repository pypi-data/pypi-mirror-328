"""
Financial Modeling Prep Client Library

Exposes:
    FMP: Unified REST API client.
    Logger: Logging utility.
    ConfigManager: Configuration loader.
    Session: HTTP session with rate limiting.
    StockWebsockets: WebSocket client for stock data.
    CryptoWebsockets: WebSocket client for crypto data.
    ForexWebsockets: WebSocket client for forex data.
"""

from .logger import Logger
from .config_manager import ConfigManager
from .dynamic import create_endpoint_method, attach_dynamic_functions
from .session import Session
from .fmp_client import FMP

from .fmp_websockets.stock_websocket import StockWebsockets
from .fmp_websockets.crypto_websocket import CryptoWebsockets
from .fmp_websockets.forex_websocket import ForexWebsockets

__all__ = [
    "FMP",
    "Logger",
    "ConfigManager",
    "Session",
    "StockWebsockets",
    "CryptoWebsockets",
    "ForexWebsockets",
]

__version__ = "0.0.1"
__author__ = "Vimal Seshadri Raguraman"
