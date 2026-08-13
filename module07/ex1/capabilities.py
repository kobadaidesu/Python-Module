import abc


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self) -> str:
        ...


class TransformCapability(abc.ABC):
    def __init__(self) -> None:
        self._is_transformed = False

    @abc.abstractmethod
    def transform(self) -> str:
        ...

    @abc.abstractmethod
    def revert(self) -> str:
        ...
