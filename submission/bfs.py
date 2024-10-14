#####################################################
# CS 6601 - Assignment 1͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# bfs.py͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
#####################################################

# DO NOT ADD OR REMOVE ANY IMPORTS FROM THIS FILE͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
import math

# Credits if any
# 1)
# 2)
# 3)

def return_your_name() -> str:
    """Return your first and last name from this function as a string"""
    return "Erwei Yao"


def breadth_first_search(graph, start, goal) -> list:
    """
    Warm-up exercise: Implement breadth-first-search.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start: Key for the start node.
        goal: Key for the end node.

    Returns:
        The best path via BFS as a list from the start to the goal node (including both).
    """

    if start == goal:
        return []
    
    # Initialize the queue and memo (using list instead of deque)
    queue = [[start]]  # Queue is a list of paths
    memo = set([start])  # Memo to keep track of visited nodes

    # BFS loop
    while queue:
        path = queue.pop(0)  # Use pop(0) to simulate queue behavior
        node = path[-1]

        # Explore neighbors
        for neighbor in sorted(graph.neighbors(node)):
            if neighbor == goal:
                return path + [neighbor]
            if neighbor not in memo:
                memo.add(neighbor)
                queue.append(path + [neighbor])
    
    return []
