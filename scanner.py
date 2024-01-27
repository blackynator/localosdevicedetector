import psutil

def get_connected_interfaces():
    interfaces = psutil.net_if_addrs()
    return interfaces

def get_connected_devices():
    partitions = psutil.disk_partitions()
    io_counters = psutil.disk_io_counters(perdisk=True)
    devices = partitions + list(io_counters.items())
    return devices

def main():
    connected_interfaces = get_connected_interfaces()
    connected_devices = get_connected_devices()

    print("Connected Devices:")
    for number, (interface, addresses) in enumerate(connected_interfaces.items(), start=1):
        addresses_str = ', '.join([addr.address if hasattr(addr, 'address') else addr for addr in addresses])
        print(f"{number}. {interface}: {addresses_str}")

    print("\nConnected Devices:")
    for number, device in enumerate(connected_devices, start=1):
        if isinstance(device, tuple):  # Check if it's an item from io_counters
            device_name, io_counter = device[0], device[1]
            print(f"{number}. Device: {device_name}")
   
        elif isinstance(device, psutil.sdiskpart):
            print(f"{number}. Device {device.device}")

if __name__ == "__main__":
    main()
