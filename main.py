from optparse import OptionError
from advanced_remote import AdvancedRemote
from device import Device
from remote import Remote
from radio import Radio
from tv import TV
from smart_tv import SmartTV

option: int = -1

print('Seleccionar dispositivo')
print('1. Radio')
print('2. TV')
print('3. SmartTV')
selected_device = int(input('Seleccionar opción: '))
device: Device

if selected_device == 1:
    device = Radio()
elif selected_device == 2:
    device = TV()
elif selected_device == 3:
    device = SmartTV()
else:
    print('Opción inválida')
    raise OptionError

print('Seleccionar control')
print('1. Control normal')
print('2. Control avanzado')
selected_remote = int(input('Seleccionar opción: '))
remote: Remote

if selected_remote == 1:
    remote = Remote(device)
elif selected_remote == 2:
    remote = AdvancedRemote(device)
else:
    print('Opción inválida')
    raise OptionError


while option != 0:
    print('1. Estado del dispositivo')
    print('2. Encender/apagar')
    print('3. Subir volumen')
    print('4. Bajar volumen')
    print('5. Subir canal')
    print('6. Bajar canal')
    if isinstance(remote, AdvancedRemote):
        print('7. Mute')
    print('0. Salir')
    option = int(input('Seleccionar opción: '))

    if option == 1:
        remote.get_device_status()
    elif option == 2:
        remote.toggle_power()
    elif option == 3:
        remote.volume_up()
    elif option == 4:
        remote.volume_down()
    elif option == 5:
        remote.channel_up()
    elif option == 6:
        remote.channel_down()
    elif option == 7 and isinstance(remote, AdvancedRemote):
        remote.mute()
    else:
        print('Opcion incorrecta')
