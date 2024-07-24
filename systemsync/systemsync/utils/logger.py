from enum import Enum


class LogSource(Enum):
    MAIN = "[GLOBAL]"
    ACTION = "[ACTION]"


class LogPrefix(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"


class Logger:
    """
    Logging utility class
    """

    @staticmethod
    def log(prefix: LogPrefix, source: LogSource, text: str) -> None:
        print(f"{source.value}[{prefix.value}] {text}")

    @staticmethod
    def debug(source: LogSource, text: str) -> None:
        return Logger.log(LogPrefix.DEBUG, source, text)

    @staticmethod
    def info(source: LogSource, text: str) -> None:
        return Logger.log(LogPrefix.INFO, source, text)

    @staticmethod
    def warn(source: LogSource, text: str) -> None:
        return Logger.log(LogPrefix.WARN, source, text)

    @staticmethod
    def error(source: LogSource, text: str) -> None:
        return Logger.log(LogPrefix.ERROR, source, text)
