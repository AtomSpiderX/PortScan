# 🔍 Port Scanner with Vulnerability Checker

A simple Python tool that scans a target for open ports, attempts basic banner grabbing, and checks for known vulnerabilities using the CVE API.

## 🚀 Features

- TCP port scanner
- Banner grabbing
- Checks CVEs from [cve.circl.lu](https://cve.circl.lu/)
- Lightweight and beginner-friendly

## 🛠️ Usage

```bash
pip install -r requirements.txt
python scanner.py <target> --ports 22,80,443
