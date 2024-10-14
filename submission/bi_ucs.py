#####################################################
# CS 6601 - Assignment 1͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# bi_ucs.py͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
#####################################################

# DO NOT ADD OR REMOVE ANY IMPORTS FROM THIS FILE͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
import math
from submission.priority_queue import PriorityQueue

# Credits if any͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 1)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 2)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 3)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

def bidirectional_ucs(graph, start, goal) -> list:
    """
    Implements Bidirectional Uniform Cost Search.

    Args:
        graph (ExplorableGraph): The undirected graph to search.
        start: The start node.
        goal: The goal node.

    Returns:
        The optimal path from the start to the goal node (including both start and goal).
    """

    if start==goal:
        return []
    
    f_queue=PriorityQueue();
    b_queue=PriorityQueue();

    f_explored={};
    b_explored={};

    f_queue.append((0,start,[start]));
    b_queue.append((0,goal,[goal]));

    min_cost=math.inf;
    best_path=[];

    while not f_queue.is_empty() and not b_queue.is_empty():
        #forward expanding
        f_cost,f_node,f_path=f_queue.pop();
        if f_node not in f_explored or f_cost<f_explored[f_node][0]:
            f_explored[f_node]=(f_cost,f_path)
            #meeting backward node
            if f_node in b_explored:
                total_cost=f_cost+b_explored[f_node][0]
                if total_cost<min_cost:
                    min_cost=total_cost
                    #reverse, then start from the second node
                    best_path=f_path+b_explored[f_node][1][::-1][1:]
            
            #expand neighbor nodes 
            for neighbor in sorted(graph.neighbors(f_node)):
                new_cost=f_cost+graph.get_edge_weight(f_node,neighbor)
                if neighbor not in f_explored or new_cost<f_explored[neighbor][0]:
                    f_queue.append((new_cost,neighbor,f_path+[neighbor]))

        #backward expanding
        b_cost,b_node,b_path=b_queue.pop()
        if b_node not in b_explored or b_cost<b_explored[b_node][0]:
            b_explored[b_node]=(b_cost,b_path)
            #meeting forward node
            if b_node in f_explored:
                total_cost=b_cost+f_explored[b_node][0]
                if total_cost<min_cost:
                    min_cost=total_cost
                    best_path=f_explored[b_node][1]+b_path[::-1][1:]
            
            #expanding the neighbors
            for neighbor in sorted(graph.neighbors(b_node)):
                new_cost=b_cost+graph.get_edge_weight(b_node,neighbor)
                if neighbor not in b_explored or new_cost<b_explored[b_node][0]:
                    b_queue.append((new_cost,neighbor,b_path+[neighbor]))
        
        #condition testing
        if not f_queue.is_empty() and not b_queue.is_empty():
            if f_queue.top()[0]+b_queue.top()[0]>=min_cost:
                break

    return best_path




