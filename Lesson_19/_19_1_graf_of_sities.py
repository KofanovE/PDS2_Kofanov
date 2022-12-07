# Використовуючі дані із файлу cities.csv, створіть список типу: cities = [["citi1", "citi2", km]...].
# З отриманого списку створіть граф. Візуалізуйте отриманий граф.

import networkx as nx
import matplotlib.pyplot as plt

edgelist = []
with open("cities.csv") as file:
    for line in file:
        city_1, city_2, distance = line.strip().split(";")
        edgelist.append([city_1, city_2, distance])

graph = nx.Graph()
for edge in edgelist:
    graph.add_edge(edge[0], edge[1], weight = int(edge[2]))

pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos)
plt.title("Graph of Ukrainian cities")
plt.show()

