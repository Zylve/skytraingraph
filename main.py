from pyvis.network import Network
import graph
import station_network


station_map = graph.Graph()

station_network.register_stations(station_map)
station_network.register_edges(station_map)

net = Network(notebook=True, cdn_resources="remote",
    bgcolor = "#222222",
    font_color = "white",
    height = "750px",
    width = "100%",
    select_menu=True,
    filter_menu=True
)

net.add_nodes([n.name for n in station_map.nodes])
net.add_edges([(e.start.name, e.end.name, 10) for e in station_map.edges])
net.show_buttons(filter_=['physics', 'layout', 'interaction', 'edges'])
net.show("graph.html")