from logging import Logger

class PrintLogger(Logger):
    """
    A logger that prints to console.
    """

    def __init__(self) -> None:
        pass

    def debug(self, log: str) -> None:
        print(f"[D] {log}")

    def info(self, log: str) -> None:
        print(f"[I] {log}")

    def warning(self, log: str) -> None:
        print(f"[W] {log}")

    def error(self, log: str) -> None:
        print(f"[E!] {log}")