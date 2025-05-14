import requests
import socket

# Mapping of common ports to service names
PORTS_TO_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Proxy",
}

def get_banner(sock):
    try:
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024).decode().strip()
        return banner
    except:
        return None

def get_service_name(port):
    return PORTS_TO_SERVICES.get(port, "Unknown")

def check_cve(service_banner):
    cve_api = "https://cve.circl.lu/api/search/"
    try:
        keywords = service_banner.split("/")
        if len(keywords) > 0:
            query = keywords[0]
            response = requests.get(cve_api + query)
            if response.status_code == 200:
                cve_data = response.json()
                cves = [item['id'] for item in cve_data.get('data', [])]
                return cves
    except Exception as e:
        print(f"[-] Error checking CVEs: {e}")
    return []
