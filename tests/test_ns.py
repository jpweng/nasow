from nasow.add_ns import dns_to_write


def test_ns():
    dns_from_windows = ["nameserver 172.20.10.1", "nameserver 172.88.10.2"]
    dns_in_wsl = ["nameserver 172.99.88.1", "nameserver 172.88.10.2"]
    expected = ["nameserver 172.20.10.1", "nameserver 172.88.10.2", "nameserver 172.99.88.1"]
    assert dns_to_write(dns_from_windows, dns_in_wsl) == expected
