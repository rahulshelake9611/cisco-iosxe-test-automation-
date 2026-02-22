import pytest
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': 'devnetsandboxiosxec9k.cisco.com',
    'username': 'rahulshelake9611',
    'password': '-Kg62wa4_pNh-CjO',
}

@pytest.fixture
def ssh_connection():
    connection = ConnectHandler(**device)
    yield connection
    connection.disconnect()

def test_interface_status(ssh_connection):
    output = ssh_connection.send_command("show ip interface brief")
    assert "GigabitEthernet1" in output
    assert "up" in output