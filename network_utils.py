from netmiko import ConnectHandler

devnet_sandbox = {
    'device_type': 'cisco_ios',
    'host': 'devnetsandboxiosxec9k.cisco.com',
    'username': 'rahulshelake9611',
    'password': '-Kg62wa4_pNh-CjO',
    'port': 22,
}

# The connection logic
try:
    with ConnectHandler(**devnet_sandbox) as net_connect:
        print("Successfully connected to Cisco Sandbox!")
        
        output = net_connect.send_command("show version")
        print(output)