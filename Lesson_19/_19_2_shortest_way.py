# Напишіть функцію знаходження найкоротшого маршруту між двома населенними пунктами,
# яка приймає в якості аргументів об'єкт графу і пару населених пунктів, а повертає
# маршрут і його протяжність.

import networkx as nx

def main():

    edgelist = []
    with open("cities.csv") as file:
        for line in file:
            city_1, city_2, weight = line.strip().split(";")
            edgelist.append([city_1, city_2, weight])

    graph = nx.Graph()
    for edge in edgelist:
        graph.add_edge(edge[0], edge[1], weight = int(edge[2]))

    short_way(graph, 'Kremenchuk', 'Novomoskovsk')


def short_way(g, city_1, city_2):
    way = nx.shortest_path(g, city_1, city_2, weight = "weight")
    distance = nx.shortest_path_length(g, city_1, city_2, weight = 'weight')
    i = 0
    print("The shortest way: ", end="")
    for city in way:
        if i > 0:
            print(" -> ", end="")
        print(city, end="")
        i += 1
    print(f"\nDistance: {distance}")






if __name__ == "__main__":
    main()