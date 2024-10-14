#####################################################
# CS 6601 - Assignment 1͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# tri_ucs.py͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
#####################################################

# DO NOT ADD OR REMOVE ANY IMPORTS FROM THIS FILE͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
from submission.priority_queue import PriorityQueue

def tridirectional_search(graph, goals):
    if len(set(goals)) == 1:
        return []
    
    if len(set(goals)) == 2:
        start = goals[0]
        end = next(g for g in goals if g != start)
        return unidirectional_ucs(graph, start, end)
    
    frontiers = [PriorityQueue() for _ in range(3)]
    explored = [{}, {}, {}]
    parents = [{}, {}, {}]
    
    for i, goal in enumerate(goals):
        frontiers[i].append((0, goal, 0))
        explored[i][goal] = 0
    
    best_path = None
    best_cost = float('inf')
    
    while all(not f.is_empty() for f in frontiers):
        for i in range(3):
            if frontiers[i].is_empty():
                continue
            
            _, node, cost = frontiers[i].pop()
            
            if cost > best_cost:
                return best_path
            
            # Check if this node is common in any other search fronts
            for j in range(3):
                if j != i and node in explored[j]:
                    path1 = reconstruct_path(parents[i], goals[i], node)
                    path2 = reconstruct_path(parents[j], goals[j], node)
                    # Only merge paths when the shared path is valid (avoid redundant nodes)
                    if path1[-1] == path2[-1]:  # Merge at the common node
                        full_path = path1[:-1] + path2[::-1]
                    else:
                        full_path = path1 + path2[::-1][1:]
                    
                    path_cost = cost + explored[j][node]
                    
                    # Ensure the path touches all three goals and is optimal
                    if len(set(goals) & set(full_path)) == 3 and path_cost < best_cost:
                        best_path = full_path
                        best_cost = path_cost
            
            # Explore neighbors
            for neighbor in sorted(graph.neighbors(node)):
                new_cost = cost + graph.get_edge_weight(node, neighbor)
                
                # Update only if we found a better cost path
                if neighbor not in explored[i] or new_cost < explored[i][neighbor]:
                    explored[i][neighbor] = new_cost
                    parents[i][neighbor] = node
                    frontiers[i].append((new_cost, neighbor, new_cost))
    
    return best_path

def reconstruct_path(parents, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parents[path[-1]])
    return path[::-1]

def unidirectional_ucs(graph, start, goal):
    frontier = PriorityQueue()
    frontier.append((0, start, 0))
    explored = {start: 0}
    parents = {}
    
    while not frontier.is_empty():
        _, node, cost = frontier.pop()
        
        if node == goal:
            return reconstruct_path(parents, start, goal)
        
        for neighbor in sorted(graph.neighbors(node)):
            new_cost = cost + graph.get_edge_weight(node, neighbor)
            if neighbor not in explored or new_cost < explored[neighbor]:
                explored[neighbor] = new_cost
                parents[neighbor] = node
                frontier.append((new_cost, neighbor, new_cost))
    
    return None
