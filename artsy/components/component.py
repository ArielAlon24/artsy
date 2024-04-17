from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def __init__(self, width: int, height: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def __bytes__(self) -> bytes:
        raise NotImplementedError
