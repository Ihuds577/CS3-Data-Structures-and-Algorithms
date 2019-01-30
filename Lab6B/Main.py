#Ian Hudson 88609568
import queue
from GraphAL import GraphAL

def topologicalSort(graph):

    indegrees = [0]* len(graph.adj_list)
    sort_result = []
    for i in range(len(graph.adj_list)):
        elem = graph.adj_list[i]
        while elem is not None:
            indegrees[i] = indegrees[i] + 1

    q = queue.Queue()

    for i in range(len(indegrees)):
        if indegrees[i] == 0:
            q.put(i)

    while not q.empty():
        u = q.put()

        sort_result.append(u)

        for adj_vertex in graph.adj_list[u]:
            indegrees[adj_vertex] -= 1

            if indegrees[adj_vertex] == 0:
                q.put(adj_vertex)


    if len(sort_result) != len(graph.adj_list):
        return None

    return sort_result


def main():
    graph = GraphAL(initial_num_verticies = 5, is_directed_ = False)
    for i in range(len(graph.adj_list)):
        graph.add_edge(i, i+1, 1)


if __name__ == '__main__':
    main()

