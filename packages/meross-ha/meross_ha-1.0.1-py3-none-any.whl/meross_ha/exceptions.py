"""Meross exceptions."""
from __future__ import annotations


class MerossError(Exception):
    """Base class for aioRefoss errors."""


class InvalidMessage(MerossError):
    """Exception raised when an invalid message is received."""


class DeviceTimeoutError(MerossError):
    """Exception raised when http request timeout."""


class SocketError(MerossError):
    """Exception raised when socket send msg."""
