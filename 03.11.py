import scapy.all as scapy


def sniffing (interface):
    a = scapy.sniff(iface = interface,count = 5, store = False,  filter = 'tcp',prn = process_packet)


def process_packet(packet):
    stream = packet.show()
    print(stream)
    return stream

sniffing(None)

def save_data_to_file(stream):
    with open(stream, "w") as file:
        file.write(stream)
        
save_data_to_file(process_packet())
