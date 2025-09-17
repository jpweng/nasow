import subprocess
import json
from pathlib import Path


def get_dns_servers():
    '''
    Get the DNS servers on this Windows machine
    '''
    cmd = [
        'powershell', '-NoProfile', '-Command',
        "Get-DnsClientServerAddress -AddressFamily IPv4 | Where-Object {$_.ServerAddresses -ne $null} | Select-Object -ExpandProperty ServerAddresses | ConvertTo-Json"
    ]
    output = subprocess.check_output(cmd, universal_newlines=True)
    servers = json.loads(output)
    if not isinstance(servers, list):
        servers = [servers]
    return list(set([f"nameserver {s}" for s in servers]))


def dns_from_wsl():
    '''
    Read the current /etc/resolv.conf in WSL and return a list of lines that start with "nameserver"
    '''
    wsl_path = Path(r"\\wsl.localhost\Ubuntu-20.04\etc\resolv.conf")
    if not wsl_path.exists():
        print(f"WSL resolv.conf not found at {wsl_path}")
        return []
    with open(wsl_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
    return [line for line in lines if line.startswith("nameserver")]


def dns_to_write(dns_from_windows, dns_in_wsl):
    '''
    Given two lists of dns server lines, return a list that contains all unique lines
    preserving the order of the first list and appending any new lines from the second list
    '''
    result = dns_from_windows  # Start with all from Windows
    for line in dns_in_wsl:
        if line not in result:
            result.append(line)
    return result


def copy_to_wsl_resolv_conf(dns, wsl_distro="Ubuntu-20.04"):
    # UNC path
    dns_text = "\n".join(dns) + "\n"
    wsl_path = f"\\\\wsl.localhost\\{wsl_distro}\\etc\\resolv.conf"
    try:
        with open(wsl_path, 'w', encoding='utf-8', newline='\n') as dst:
            dst.write(dns_text)
    except Exception as e:
        print(f"Failed to copy resolv.conf to WSL: {e}")


if __name__ == "__main__":
    print("Obtaining DNS servers from Windows")
    servers = get_dns_servers()
    print("DNS servers to add")
    print(servers)

    print("Reading current DNS servers from WSL")
    current_dns = dns_from_wsl()
    print("Current DNS servers in WSL")
    print(current_dns)

    dns = dns_to_write(servers, current_dns)
    print("Final DNS servers to write to WSL")
    print(dns)

    print("Copying to WSL")
    copy_to_wsl_resolv_conf(dns)
