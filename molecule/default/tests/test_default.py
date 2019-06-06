import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hostname(host):
    cmd = host.run("hostname -f")
    ihost = host.ansible.get_variables()["inventory_hostname"]

    assert cmd.stdout == ihost
