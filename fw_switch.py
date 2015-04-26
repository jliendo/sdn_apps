from ryu.lib.ip import ipv4_to_bin

from switch import Switch


class FWSwitch(Switch):

    def __init__(self, *args, **kwargs):
        super(FWSwitch, self).__init__(*args, **kwargs)

    def permit_packet(self, dp, parser, pkt):
        if pkt is not None:
            if pkt.src_ip == "10.0.0.1" and pkt.dst_ip == "10.0.0.2":
                match = parser.OFPMatch(
                    eth_type=0x0800,
                    ipv4_src="10.0.0.1",
                    ipv4_dst="10.0.0.2",
                )
                actions = []
                priority = 10
                self.add_flow(dp, priority, match, actions)
                return False
        return True
