import nmap
def scan_ports(target_ip, port_range):
    """

    สแกนพอร์ตเป้าหมาย IP
    Args:
         target_ip (str): IP address ของเป้าหมาย
         port_range (str): ช่วงพอร์ตที่ต้องการสแกน (เช่น "20-80")
    """

    nm = nmap.PortScanner()

    try:
        nm.scan(target_ip, port_range)

        for host in  nm.all_hosts():
            print(f"host: {host} ({nm[host].hostname()})")
            for proto in nm[host].all_protocols():
                print(f"Protocol: {proto}")

                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")

    except nmap.PortScannerError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    port_range = input("Enter the port range (e.g. 20-80): ")

    scan_ports(target_ip, port_range)
