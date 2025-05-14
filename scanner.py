import socket
import argparse
from utils import get_banner, get_service_name, check_cve
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def scan_target(target, ports):
    print(f"\nScanning target: {target}\n{'-'*50}")
    for port in ports:
        service = get_service_name(port)  # Get the service name (e.g., HTTP, SSH)
        try:
            sock = socket.socket()
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open ({service})")
                banner = get_banner(sock)
                if banner:
                    # Highlight version in green
                    print(f"    Banner: {Fore.GREEN + banner + Style.RESET_ALL}")
                    cves = check_cve(banner)
                    if cves:
                        print("    Potential CVEs:")
                        for cve in cves[:5]:
                            print(f"     - {cve}")
            sock.close()
        except Exception as e:
            print(f"[-] Error on port {port}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner with Vulnerability Check")
    parser.add_argument("target", help="IP address or domain to scan")
    parser.add_argument("--ports", help="Ports to scan (comma-separated)", default="21,22,23,25,53,80,110,143,443,3306,8080")
    args = parser.parse_args()

    target = args.target
    ports = list(map(int, args.ports.split(",")))
    scan_target(target, ports)

if __name__ == "__main__":
    main()
