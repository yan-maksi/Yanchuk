import scapy.all as scapy


def sniffing (interface):
    a = scapy.sniff(iface = interface,count = 5, store = False,  filter = 'tcp',prn = process_packet)


def process_packet(packet):
    print(packet.show())


sniffing(None)
