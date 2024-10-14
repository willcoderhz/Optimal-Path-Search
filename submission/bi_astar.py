#####################################################
# CS 6601 - Assignment 1͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# bi_astar.py͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
#####################################################

# DO NOT ADD OR REMOVE ANY IMPORTS FROM THIS FILE͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
import math

from submission.astar import euclidean_dist_heuristic
from submission.priority_queue import PriorityQueue

# Credits if any͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 1)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 2)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 3)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁


import math

def bidirectional_a_star(graph, start, goal, heuristic=euclidean_dist_heuristic) -> list:
    """
    Implements bidirectional A* algorithm to find the shortest path from start to goal.
    
    Args:
        graph (ExplorableGraph): The graph to search on.
        start: The starting node.
        goal: The goal node.
        heuristic: Heuristic function to estimate distance between nodes.
        
    Returns:
        list: The shortest path from start to goal (inclusive), or an empty list if start == goal.
    """
    
    if start == goal:
        return []

    f_queue = PriorityQueue()  
    b_queue = PriorityQueue()  
    f_visited = {start: 0}     
    b_visited = {goal: 0}      
    f_parents = {start: None}  
    b_parents = {goal: None}   
    f_queue.append((0 + heuristic(graph, start, goal), start, 0))
    b_queue.append((0 + heuristic(graph, goal, start), goal, 0))
    min_cost = math.inf
    best_meeting_node = None

    
    def constructor(best_meeting_node):
        f_path = []
        b_path = []

        node = best_meeting_node
        while node is not None:
            f_path.append(node)
            node = f_parents[node]
        
        node = b_parents[best_meeting_node]  
        while node is not None:
            b_path.append(node)
            node = b_parents[node]
        
        return f_path[::-1] + b_path 

  
    while not f_queue.is_empty() and not b_queue.is_empty():
        top_f = f_queue.top()[0] 
        top_r = b_queue.top()[0]  

       
        if top_f + top_r >= min_cost + heuristic(graph, start, goal):
            break

       
        _, current_fnode, current_fcost = f_queue.pop()

        if current_fnode in b_visited:
            total_cost = current_fcost + b_visited[current_fnode]
            if total_cost < min_cost:
                min_cost = total_cost
                best_meeting_node = current_fnode
        
        for neighbor in sorted(graph.neighbors(current_fnode)):
            new_cost = current_fcost + graph.get_edge_weight(current_fnode, neighbor)
            if neighbor not in f_visited or new_cost < f_visited[neighbor]:
                f_visited[neighbor] = new_cost
                f_parents[neighbor] = current_fnode
                f_queue.append((new_cost + heuristic(graph, neighbor, goal), neighbor, new_cost))
        
    
        _, current_bnode, current_bcost = b_queue.pop()

        if current_bnode in f_visited:
            total_cost = f_visited[current_bnode] + current_bcost
            if total_cost < min_cost:
                min_cost = total_cost
                best_meeting_node = current_bnode

        for neighbor in sorted(graph.neighbors(current_bnode)):
            new_cost = current_bcost + graph.get_edge_weight(current_bnode, neighbor)
            if neighbor not in b_visited or new_cost < b_visited[neighbor]:
                b_visited[neighbor] = new_cost
                b_parents[neighbor] = current_bnode
                b_queue.append((new_cost + heuristic(graph, neighbor, start), neighbor, new_cost))

    if best_meeting_node is not None:
        return constructor(best_meeting_node)


    return []

    
   