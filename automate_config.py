from netmiko import ConnectHandler
import time

# Load device list
with open('device_list.txt') as f:
    devices = f.read().splitlines()

# Load configuration commands
with open('config_commands.txt') as f:
    config_commands = f.read().splitlines()

# Loop through each device and send config
for device in devices:
    ip, device_type, username, password = device.split(',')

    device_info = {
        'device_type': f'{device_type}_ios',
        'ip': ip,
        'username': username,
        'password': password,
    }

    print(f"\nConnecting to {ip}...")
    try:
        net_connect = ConnectHandler(**device_info)
        output = net_connect.send_config_set(config_commands)
        print(f"Configuration output for {ip}:\n{output}")
        net_connect.disconnect()
    except Exception as e:
        print(f"Failed to connect to {ip}: {str(e)}")

    time.sleep(1)
