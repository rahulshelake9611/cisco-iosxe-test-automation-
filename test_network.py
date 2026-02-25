import pytest
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_nxos',
    'host': 'devnetsandboxiosxec9k.cisco.com',
    'username': 'rahulshelake9611',
    'password': 'X4P-6-5eBS4cvVpZ',
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
