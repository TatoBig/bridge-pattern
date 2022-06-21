from device import Device


class Radio(Device):
    def __init__(self) -> None:
        self.__enable: bool = False
        self.__volume: float = 0.10
        self.__channel: int = 0
        self.__channel_list: list[str] = ['90.1', '90.3', '90.5', '90.7', '90.9', '91.0']

    def is_enabled(self) -> bool: 
        return self.__enable

    def enable(self) -> None:
        self.__enable = True
        
    def disable(self) -> None:
        self.__enable = False
    
    def get_volume(self) -> float:
        return self.__volume

    def set_volume(self, percent: float) -> None:
        if self.__volume > 0 and self.__volume < 1: 
            self.__volume = percent

    def get_channel(self) -> int:
        return self.__channel
    
    def set_channel(self, channel: int) -> None:
        if channel == -1:
            self.__channel = len(self.__channel_list) - 1
        elif channel == len(self.__channel_list):
            self.__channel = 0
        else:
            self.__channel = channel
    
    def get_status(self) -> None:
        print('Estado: ', 'Encendido' if self.__enable is True else 'Apagado')
        print(f'Volumen {self.__volume*100}%, Frecuencia: {self.__channel_list[self.__channel]}')