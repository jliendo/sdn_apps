from switch import Switch


class FWSwitch(Switch):

    def __init__(self, *args, **kwargs):
        super(FWSwitch, self).__init__(*args, **kwargs)

    def permit_packet(self, pkt):
        if pkt is not None:
            print "arp.src_ip: %s" % pkt.src_ip
            print "arp.dst_ip: %s" % pkt.dst_ip
            if pkt.src_ip == "10.0.0.1" and pkt.dst_ip == "10.0.0.2":
                return False
        return True
