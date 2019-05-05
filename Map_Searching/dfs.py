# Deep first Search
from Graph import mapGraph

graph, dist= mapGraph()

class Node:
    def __init__(self, city_name):
        self.city_name = city_name
        self.children = []


class Tree:
    def __init__(self, city_name):
        self.root = Node(city_name)

    def bubble_sort(self, name_list):
        count = len(name_list)
        for i in range(0, count):
            for j in range(i + 1, count):
                if name_list[i] > name_list[j]:
                    name_list[i], name_list[j] = name_list[j], name_list[i]
        return name_list

    def add_children(self):
        g = self.bubble_sort(graph[self.root.city_name])
        for child in g:
            self.root.children.append(Node(child))
        return self.root.children

    def get_Children_name(self):
        child_list = []
        for child in self.add_children():
            child_list.append(child.city_name)
        return child_list

class dfs_Search:
    def __init__(self, start_name, end_name):
        self.start_city = Node(start_name)
        self.end_city = Node(end_name)



    def find_endcity(self):
        stack = []
        path = {}
        num_node = 0
        stack.append(self.start_city)
        path[self.start_city.city_name] = (self.start_city.city_name)
        while(stack):
            node = stack.pop()
            name = node.city_name
            num_node += 1
            if name != self.end_city.city_name:
                if Tree(name).add_children() == [] or all([i in path for i in Tree(name).get_Children_name()]):
                    del path[name]
                    continue
                else:
                    for child in Tree(name).get_Children_name():
                        if child not in path.viewkeys():
                            stack.append(Node(child))
                            tem_tuple = path[name]
                            path[child] = ((tem_tuple) +(' -> ') + (child))

            else:
                gn = []
                new_list = path[node.city_name].split(' -> ')
                for i in range(len(new_list) - 1):
                    gn.append(dist[new_list[i + 1] + new_list[i]])
                return path[node.city_name], num_node, sum(gn)
                break
