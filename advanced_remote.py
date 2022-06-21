from device import Device
from remote import Remote


class AdvancedRemote(Remote):
    def __init__(self, device: Device) -> None:
        super().__init__(device)

    def mute(self) -> None:
        self.device.set_volume(0)