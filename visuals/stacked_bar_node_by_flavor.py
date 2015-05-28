from collections import OrderedDict
from itertools import chain, repeat

import numpy as np

import matplotlib.pyplot as plt


DATA_PATH = "~/dev/bio5/cloaked-sombrero/data/nodes_by_flavor.txt"


def get_data():
    return open(os.path.expanduser(DATA_PATH)).readlines()[1:]


def by_node(data):
    """
    Split lines from OpenStack mysql nova database by node, flavor
    and the count of that flavor per node into a dictionary of
    dictionaries.
    """
    coll = {}
    for line in data:
        val, flavor, node = line.split()
        if not node in coll.keys():
            coll[node] = {}
        coll[node][flavor] = int(val)
    return coll


def by_flavor(nodes):
    """
    Transform nodes collection to group by flavors for visualization.
    """
    flavor_names = set(
        chain(
            *[fd.keys() for node, fd in nodes.iteritems()]))
    coll = OrderedDict({f: [] for f in flavor_names})
    node_names = nodes.keys()
    node_names.sort()
    for node_name in node_names:
        for flavor_name in flavor_names:
            if flavor_name in nodes[node_name].keys():
                coll[flavor_name].append(nodes[node_name][flavor_name])
            else:
                coll[flavor_name].append(0)
    return coll


def build_visual(data):
    nodes = by_node(data)
    flavors = by_flavor(nodes)
    flavor_size = len(flavors.keys())
    node_names = sorted(nodes.keys())
    node_size = len(nodes.keys())
    btm = [0] * node_size
    ind = np.arange(0, node_size * 1.5, 1.5)
    width = 0.86
    colors= ["r", "b", "g", "dimgray", "darkcyan", "lime",
             "navy", "teal", "indigo", "y", "skyblue", "sage"]
    color_labels = []
    c = 0
    plt.xticks(ind + width/2., node_names, rotation=70)
    plt.title("Node resource usage by flavor")
    for f,v in flavors.iteritems():
        b = plt.bar(ind,
                    v,
                    width,
                    color=colors[c % len(colors)],
                    bottom=btm)
        color_labels.append(b[0])
        c += 1
        btm = [f + b for f, b in zip(btm, v)]
    plt.legend(color_labels, flavors.keys())

build_visual(get_data())
plt.show()
