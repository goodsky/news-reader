from logging import Logger
from enum import Enum


class LogLevel(Enum):
    Error = 0
    Warning = 1
    Info = 2
    Debug = 3


class PrintLogger(Logger):
    """
    A logger that prints to console.
    """

    def __init__(self, log_level: LogLevel = LogLevel.Info) -> None:
        self.log_level = log_level

    def debug(self, log: str) -> None:
        if self.log_level.value >= LogLevel.Debug.value:
            print(f"[Debug] {log}")

    def info(self, log: str) -> None:
        if self.log_level.value >= LogLevel.Info.value:
            print(f"[Info] {log}")

    def warning(self, log: str) -> None:
        if self.log_level.value >= LogLevel.Warning.value:
            print(f"[Warning] {log}")

    def error(self, log: str) -> None:
        if self.log_level.value >= LogLevel.Error.value:
            print(f"[ERROR!] {log}")
