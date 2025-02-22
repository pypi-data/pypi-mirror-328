"""Telegram Transfer

一个基于Telethon的Telegram文件传输工具，支持文件夹上传、下载和同步功能。
"""

from .client import TelegramTransferClient
from .cli import cli

__version__ = '0.0.0.dev202502200709'
__all__ = ["TelegramTransferClient", "cli"]