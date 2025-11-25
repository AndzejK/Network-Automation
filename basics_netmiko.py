from netmiko import ConnectHandler

# https://devnetsandbox.cisco.com

cisco_sandbox={
    'device_type': 'cisco_ios',  
    'host':   'sandbox-iosxr-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port': 22
}

print(f'Connecting to Cisco DevNet Sandbox...')

# Error Handling
try:
    net_connect=ConnectHandler(**cisco_sandbox)
    print(f'\nConnected successfully!')

    # Sending a cisco command to get version of the device
    output=net_connect.send_command('show version')
    print("\n=== Device Information ===")
    print(output)

except Exception as e:
    print(f'Connection failed: {e}')