import evdev

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in devices:
    print(device.path, device.name, device.phys)

device = evdev.InputDevice('/dev/input/event1')

print(device)

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
    if event.type == 3:  # A stick is moved
        if event.code == 4:
            print(f"{event}")
# python -m evdev.evtest
