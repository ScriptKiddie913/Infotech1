from scapy.all import sniff, IP, TCP, UDP, ICMP

def extract_flags_and_pointers(packet):
    """Extract flags and pointers from TCP packets."""
    if TCP in packet:
        tcp_flags = packet[TCP].flags
        flags = {
            'URG': 'U' in tcp_flags,
            'ACK': 'A' in tcp_flags,
            'PSH': 'P' in tcp_flags,
            'RST': 'R' in tcp_flags,
            'SYN': 'S' in tcp_flags,
            'FIN': 'F' in tcp_flags
        }
        return flags
    return None

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        data = packet[IP].payload
        
        # Attempt to extract and decode data
        try:
            data = data.load.decode(errors='ignore')
        except AttributeError:
            data = ''
        
        # Map protocol number to name
        protocol_map = {
            1: 'ICMP',
            6: 'TCP',
            17: 'UDP'
        }
        protocol_name = protocol_map.get(protocol, 'Unknown')

        # Extract flags and pointers if protocol is TCP
        flags = extract_flags_and_pointers(packet)
        
        # Output the packet information
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {protocol_name}")
        print(f"Data: {data}")
        
        if protocol_name == 'TCP' and flags:
            print("Flags:")
            for flag, is_set in flags.items():
                print(f"  {flag}: {is_set}")
        
        print("-" * 40)

# Start sniffing
sniff(prn=packet_callback, filter="ip", store=0)
