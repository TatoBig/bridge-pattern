from device import Device

class Remote:
    def __init__(self, device: Device) -> None:
        self.__device: Device = device
    
    @property
    def device(self) -> None:
        return self.__device

    def toggle_power(self) -> None:
        if self.__device.is_enabled():
            self.__device.disable()
        else:
            self.__device.enable()
    
    def volume_down(self) -> None:
        self.__device.set_volume(self.__device.get_volume() - 0.01)
    
    def volume_up(self) -> None:
        self.__device.set_volume(self.__device.get_volume() + 0.01)

    def channel_down(self) -> None:
        self.__device.set_channel(self.__device.get_channel() - 1)

    def channel_up(self) -> None:
        self.__device.set_channel(self.__device.get_channel() + 1)

    def get_device_status(self) -> None:
        self.__device.get_status()
