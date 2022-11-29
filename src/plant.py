import bluetooth

def connectTarget():
    target_name = "BluetoothSpeaker"
    target_addr = None
    nearby_devices = bluetooth.discover_devices()
    
    for bdaddr in nearby_devices:
        if target_name == bluetooth.lookup_name( bdaddr ):
            target_address = bdaddr
            break
    if target_addr is not None:
        print("Found Target Addr: ", target_addr)
    else:
        print("could not find bluetooth device")

if __name__ == "__main__":
    print("python correcting interpreting")
