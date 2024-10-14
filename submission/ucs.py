import math
from submission.priority_queue import PriorityQueue

def uniform_cost_search(graph, start, goal):

    if start==goal:
        return []
    
    frontier=PriorityQueue();
    frontier.append((0,(start,[start])))
    explored={}

    while not frontier.is_empty():
        current_cost,(current_node,path)=frontier.pop();

        if current_node==goal:
            return path;
        if current_node in explored and explored[current_node]<current_cost:
            continue;

        explored[current_node]=current_cost;

        for neighbor in sorted(graph.neighbors(current_node)):
            new_cost=current_cost+graph.get_edge_weight(current_node,neighbor);
            new_path=path+[neighbor];
            if (neighbor not in explored) or (new_cost<explored[neighbor]):
                frontier.append((new_cost,(neighbor,new_path)))
    
    return []

