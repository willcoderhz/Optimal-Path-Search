#####################################################
# CS 6601 - Assignment 1͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# tri_astar.py͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
#####################################################

# DO NOT ADD OR REMOVE ANY IMPORTS FROM THIS FILE͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
import math
from submission.priority_queue import PriorityQueue
from submission.astar import euclidean_dist_heuristic

# Credits if any͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 1)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 2)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 3)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

def tridirectional_upgraded(graph, goals, heuristic=euclidean_dist_heuristic):
    if len(set(goals)) == 1:
        return []
    
    if len(set(goals)) == 2:
        return bidirectional_a_star(graph, goals[0], goals[1], heuristic)
    
    g1, g2, g3 = goals
    
    # Find the center node
    center = min(graph.nodes, key=lambda n: sum(heuristic(graph, n, g) for g in goals))
    
    # Find paths from center to each goal
    paths = [a_star(graph, center, goal, heuristic) for goal in goals]
    
    # Combine paths
    combined_path = []
    for path in paths:
        if combined_path and path[0] == combined_path[-1]:
            combined_path.extend(path[1:])
        else:
            combined_path.extend(path[::-1])
    
    # Remove duplicates while preserving order
    final_path = []
    seen = set()
    for node in combined_path:
        if node not in seen:
            seen.add(node)
            final_path.append(node)
    
    return final_path

def a_star(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.append((0, start, [start]))
    explored = set()
    
    while not frontier.is_empty():
        _, current, path = frontier.pop()
        
        if current == goal:
            return path
        
        if current in explored:
            continue
        
        explored.add(current)
        
        for neighbor in sorted(graph.neighbors(current)):
            if neighbor not in explored:
                new_path = path + [neighbor]
                new_cost = len(new_path) - 1 + heuristic(graph, neighbor, goal)
                frontier.append((new_cost, neighbor, new_path))
    
    return []

def bidirectional_a_star(graph, start, goal, heuristic):
    forward_frontier = PriorityQueue()
    backward_frontier = PriorityQueue()
    forward_explored = {}
    backward_explored = {}
    
    forward_frontier.append((0, start, [start]))
    backward_frontier.append((0, goal, [goal]))
    
    while not forward_frontier.is_empty() and not backward_frontier.is_empty():
        # Forward search
        _, current_forward, path_forward = forward_frontier.pop()
        
        if current_forward in backward_explored:
            return path_forward[:-1] + backward_explored[current_forward][::-1]
        
        if current_forward not in forward_explored:
            forward_explored[current_forward] = path_forward
            for neighbor in sorted(graph.neighbors(current_forward)):
                if neighbor not in forward_explored:
                    new_path = path_forward + [neighbor]
                    new_cost = len(new_path) - 1 + heuristic(graph, neighbor, goal)
                    forward_frontier.append((new_cost, neighbor, new_path))
        
        # Backward search
        _, current_backward, path_backward = backward_frontier.pop()
        
        if current_backward in forward_explored:
            return forward_explored[current_backward][:-1] + path_backward[::-1]
        
        if current_backward not in backward_explored:
            backward_explored[current_backward] = path_backward
            for neighbor in sorted(graph.neighbors(current_backward)):
                if neighbor not in backward_explored:
                    new_path = [neighbor] + path_backward
                    new_cost = len(new_path) - 1 + heuristic(graph, neighbor, start)
                    backward_frontier.append((new_cost, neighbor, new_path))
    
    return []