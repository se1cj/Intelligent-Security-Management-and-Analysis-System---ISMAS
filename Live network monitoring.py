from scapy.all import sniff, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"New Packet: {ip_layer.src} -> {ip_layer.dst}")

# بدء مراقبة الشبكة
sniff(prn=packet_callback, count=0)
