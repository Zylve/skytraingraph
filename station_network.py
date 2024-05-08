import graph

stations = [
    graph.Node("waterfront_expo"),
    graph.Node("burrard"),
    graph.Node("granville"),
    graph.Node("stadium_chinatown"),
    graph.Node("main_street_science_world"),
    graph.Node("commercial_broadway_expo"),
    graph.Node("nanaimo"),
    graph.Node("twenty_ninth_ave"),
    graph.Node("joyce_collingwood"),
    graph.Node("patterson"),
    graph.Node("metrotown"),
    graph.Node("royal_oak"),
    graph.Node("edmonds"),
    graph.Node("twenty_second_street"),
    graph.Node("new_westminster"),
    graph.Node("columbia"),

    graph.Node("scott_road"),
    graph.Node("gateway"),
    graph.Node("surrey_central"),
    graph.Node("king_george"),

    graph.Node("sapperton"),
    graph.Node("braid"),
    graph.Node("lougheed_expo"),
    graph.Node("production_way_university_expo"),

    graph.Node("vcc_clark"),
    graph.Node("commercial_broadway_millenium"),
    graph.Node("renfrew"),
    graph.Node("rupert"),
    graph.Node("gilmore"),
    graph.Node("brentwood"),
    graph.Node("holdom"),
    graph.Node("sperling_burnaby_lake"),
    graph.Node("lake_city_way"),
    graph.Node("production_way_university_millenium"),
    graph.Node("lougheed_millenium"),
    graph.Node("burquitlam"),
    graph.Node("moody_centre"),
    graph.Node("inlet_centre"),
    graph.Node("coquitlam_central"),
    graph.Node("lincoln"),
    graph.Node("lafarge_lake_douglas"),

    graph.Node("waterfront_canada"),
    graph.Node("vancouver_city_centre"),
    graph.Node("yaletown_roundhouse"),
    graph.Node("olympic_village"),
    graph.Node("broadway_city_hall"),
    graph.Node("king_edward"),
    graph.Node("oakridge"),
    graph.Node("langara"),
    graph.Node("marine_drive"),
    graph.Node("bridgeport"),

    graph.Node("templeton"),
    graph.Node("sea_island"),
    graph.Node("yvr_airport"),

    graph.Node("aberdeen"),
    graph.Node("lansdowne"),
    graph.Node("richmond_brighouse"),
]

def register_stations(network: graph.Graph):
    for station in stations:
        network.nodes.append(station)

def register_edges(network):
    network.add_edge("waterfront_expo", "burrard", 100)
    network.add_edge("waterfront_expo", "waterfront_canada", 100)

    network.add_edge("burrard", "waterfront_expo", 110)
    network.add_edge("burrard", "granville", 130)

    network.add_edge("granville", "burrard", 140)
    network.add_edge("granville", "stadium_chinatown", 140)

    network.add_edge("stadium_chinatown", "granville", 140)
    network.add_edge("stadium_chinatown", "main_street_science_world", 140)

    network.add_edge("main_street_science_world", "stadium_chinatown", 140)
    network.add_edge("main_street_science_world", "commercial_broadway_expo", 140)

    network.add_edge("commercial_broadway_expo", "main_street_science_world", 140)
    network.add_edge("commercial_broadway_expo", "nanaimo", 140)
    network.add_edge("commercial_broadway_expo", "commercial_broadway_millenium", 140)

    network.add_edge("nanaimo", "commercial_broadway_expo", 140)
    network.add_edge("nanaimo", "twenty_ninth_ave", 140)

    network.add_edge("twenty_ninth_ave", "nanaimo", 140)
    network.add_edge("twenty_ninth_ave", "joyce_collingwood", 140)

    network.add_edge("joyce_collingwood", "twenty_ninth_ave", 140)
    network.add_edge("joyce_collingwood", "patterson", 140)

    network.add_edge("patterson", "joyce_collingwood", 140)
    network.add_edge("patterson", "metrotown", 140)

    network.add_edge("metrotown", "patterson", 140)
    network.add_edge("metrotown", "royal_oak", 140)

    network.add_edge("royal_oak", "metrotown", 140)
    network.add_edge("royal_oak", "edmonds", 140)

    network.add_edge("edmonds", "royal_oak", 140)
    network.add_edge("edmonds", "twenty_second_street", 140)

    network.add_edge("twenty_second_street", "edmonds", 140)
    network.add_edge("twenty_second_street", "new_westminster", 140)

    network.add_edge("new_westminster", "twenty_second_street", 140)
    network.add_edge("new_westminster", "columbia", 140)

    network.add_edge("columbia", "new_westminster", 140)
    network.add_edge("columbia", "scott_road", 140)


    network.add_edge("scott_road", "columbia", 140)
    network.add_edge("scott_road", "gateway", 140)

    network.add_edge("gateway", "scott_road", 140)
    network.add_edge("gateway", "surrey_central", 140)

    network.add_edge("surrey_central", "gateway", 140)
    network.add_edge("surrey_central", "king_george", 140)

    network.add_edge("king_george", "surrey_central", 140)


    network.add_edge("sapperton", "columbia", 140)
    network.add_edge("sapperton", "braid", 140)

    network.add_edge("braid", "sapperton", 140)
    network.add_edge("braid", "lougheed_expo", 140)

    network.add_edge("lougheed_expo", "braid", 140)
    network.add_edge("lougheed_expo", "production_way_university_expo", 140)
    network.add_edge("lougheed_expo", "lougheed_millenium", 140)

    network.add_edge("production_way_university_expo", "lougheed_expo", 140)
    network.add_edge("production_way_university_expo", "production_way_university_millenium", 140)



    network.add_edge("vcc_clark", "commercial_broadway_millenium", 110)

    network.add_edge("commercial_broadway_millenium", "vcc_clark", 140)
    network.add_edge("commercial_broadway_millenium", "renfrew", 140)
    network.add_edge("commercial_broadway_millenium", "commercial_broadway_expo", 140)

    network.add_edge("renfrew", "commercial_broadway_millenium", 140)
    network.add_edge("renfrew", "rupert", 140)

    network.add_edge("rupert", "renfrew", 140)
    network.add_edge("rupert", "gilmore", 140)

    network.add_edge("gilmore", "rupert", 140)
    network.add_edge("gilmore", "brentwood", 140)

    network.add_edge("brentwood", "gilmore", 140)
    network.add_edge("brentwood", "holdom", 140)

    network.add_edge("holdom", "brentwood", 140)
    network.add_edge("holdom", "sperling_burnaby_lake", 140)

    network.add_edge("sperling_burnaby_lake", "holdom", 140)
    network.add_edge("sperling_burnaby_lake", "lake_city_way", 140)

    network.add_edge("lake_city_way", "sperling_burnaby_lake", 140)
    network.add_edge("lake_city_way", "production_way_university_millenium", 140)

    network.add_edge("production_way_university_millenium", "lake_city_way", 140)
    network.add_edge("production_way_university_millenium", "lougheed_millenium", 140)
    network.add_edge("production_way_university_millenium", "production_way_university_expo", 140)

    network.add_edge("lougheed_millenium", "production_way_university_millenium", 140)
    network.add_edge("lougheed_millenium", "burquitlam", 140)
    network.add_edge("lougheed_millenium", "lougheed_expo", 140)

    network.add_edge("burquitlam", "lougheed_millenium", 140)
    network.add_edge("burquitlam", "moody_centre", 140)

    network.add_edge("moody_centre", "burquitlam", 140)
    network.add_edge("moody_centre", "inlet_centre", 140)

    network.add_edge("inlet_centre", "moody_centre", 140)
    network.add_edge("inlet_centre", "coquitlam_central", 140)

    network.add_edge("coquitlam_central", "inlet_centre", 140)
    network.add_edge("coquitlam_central", "lincoln", 140)

    network.add_edge("lincoln", "coquitlam_central", 140)
    network.add_edge("lincoln", "lafarge_lake_douglas", 140)

    network.add_edge("lafarge_lake_douglas", "lincoln", 140)



    network.add_edge("waterfront_canada", "waterfront_expo", 140)
    network.add_edge("waterfront_canada", "vancouver_city_centre", 140)

    network.add_edge("vancouver_city_centre", "waterfront_canada", 140)
    network.add_edge("vancouver_city_centre", "yaletown_roundhouse", 140)
    network.add_edge("vancouver_city_centre", "granville", 140)

    network.add_edge("yaletown_roundhouse", "vancouver_city_centre", 140)
    network.add_edge("yaletown_roundhouse", "olympic_village", 140)

    network.add_edge("olympic_village", "yaletown_roundhouse", 140)
    network.add_edge("olympic_village", "broadway_city_hall", 140)

    network.add_edge("broadway_city_hall", "olympic_village", 140)
    network.add_edge("broadway_city_hall", "king_edward", 140)

    network.add_edge("king_edward", "broadway_city_hall", 140)
    network.add_edge("king_edward", "oakridge", 140)

    network.add_edge("oakridge", "king_edward", 140)
    network.add_edge("oakridge", "langara", 140)

    network.add_edge("langara", "oakridge", 140)
    network.add_edge("langara", "marine_drive", 140)

    network.add_edge("marine_drive", "langara", 140)
    network.add_edge("marine_drive", "bridgeport", 140)

    network.add_edge("bridgeport", "marine_drive", 140)
    network.add_edge("bridgeport", "templeton", 140)
    network.add_edge("bridgeport", "aberdeen", 140)


    network.add_edge("templeton", "bridgeport", 140)
    network.add_edge("templeton", "sea_island", 140)

    network.add_edge("sea_island", "templeton", 140)
    network.add_edge("sea_island", "yvr_airport", 140)

    network.add_edge("yvr_airport", "sea_island", 140)


    network.add_edge("aberdeen", "bridgeport", 140)
    network.add_edge("aberdeen", "lansdowne", 140)

    network.add_edge("lansdowne", "aberdeen", 140)
    network.add_edge("lansdowne", "richmond_brighouse", 140)

    network.add_edge("richmond_brighouse", "lansdowne", 140)