#####################################################
# CS 6601 - Assignment 1͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# astar.py͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
#####################################################

# DO NOT ADD OR REMOVE ANY IMPORTS FROM THIS FILE͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
import math
from submission.priority_queue import PriorityQueue

# Credits if any͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 1)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 2)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 3)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

def null_heuristic(graph, u, v):
    """
    Null heuristic used as a base line.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        u: Key for the first node to calculate from.
        v: Key for the second node to calculate to.

    Returns:
        0
    """

    return 0


def euclidean_dist_heuristic(graph, u, v):
    pos_u=graph.nodes[u]['pos'];
    pos_v=graph.nodes[v]['pos'];
    distance=math.sqrt((pos_u[0]-pos_v[0])**2+(pos_u[1]-pos_v[1])**2);
    return round(distance,3)


def a_star(graph, start, goal, heuristic=euclidean_dist_heuristic) -> list:

    if start==goal:
        return [];

    queue=PriorityQueue();
    queue.append((0,start));
    routes={};
    g_s={start:0};
    f_s={start:heuristic(graph,start,goal)};
    memo=set();

    while not queue.is_empty():
        _,currentNode=queue.pop();
    
        ##backtracing here
        if currentNode==goal:
            path=[];
            while currentNode in routes:
                path.append(currentNode);
                currentNode=routes[currentNode];
            ##because the inital node has no previous node
            path.append(start);
            path.reverse();
            return path
        
        if currentNode in memo:
            continue;
        memo.add(currentNode)

        for neighbor in sorted(graph.neighbors(currentNode)):
            new_g_s=g_s[currentNode]+graph.get_edge_weight(currentNode,neighbor);
            if neighbor in memo:
                continue;
            
            if neighbor not in g_s or new_g_s<g_s[neighbor]:
                routes[neighbor]=currentNode;
                g_s[neighbor]=new_g_s;
                f_s[neighbor]=new_g_s+heuristic(graph,neighbor,goal);
            
            ##prevent repeated append into the priority queue

            if neighbor not in [n[1] for n in queue.queue]:
                queue.append((f_s[neighbor],neighbor))
    return []


  

