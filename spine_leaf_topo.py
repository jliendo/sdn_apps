import itertools
import argparse
import pdb

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI


class SpineLeaf(Topo):

    def __init__(self, **kwargs):
        super(SpineLeaf, self).__init__(**kwargs)

    def build(self, **kwargs):
        spines = kwargs.get('spines', 2)
        leafs = kwargs.get('leafs', 2)

        spine_switches = [
            self.addSwitch('s%d' % i) for i in range(1, spines + 1)
        ]
        leaf_switches = [
            self.addSwitch('l%d' % i) for i in range(1, leafs + 1)
        ]
        # cada leaf tiene un host
        hosts = [self.addHost('h%i' % i) for i in range(1, leafs + 1)]
        # cada host conectado a su respectivo switch leaf
        for h, s in zip(hosts, leaf_switches):
            self.addLink(h, s)
        # cada leaf conectado a todos los spines
        for link in itertools.product(spine_switches, leaf_switches):
            self.addLink(link[0], link[1])


topos = {'spine_leaf': (lambda **kwargs: SpineLeaf(**kwargs))}
