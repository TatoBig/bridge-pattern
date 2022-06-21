from abc import ABC, abstractmethod
from typing import Union


class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool: 
        raise NotImplementedError

    @abstractmethod
    def enable(self) -> None:
        raise NotImplementedError
        
    @abstractmethod
    def disable(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def get_volume(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def set_volume(self, percent: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_channel(self) -> Union[float, int, str]:
        raise NotImplementedError
    
    @abstractmethod
    def set_channel(self, channel: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_status(self) -> None:
        raise NotImplementedError
        