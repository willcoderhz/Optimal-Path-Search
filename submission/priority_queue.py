#####################################################
# CS 6601 - Assignment 1͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# priority_queue.py͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
#####################################################

# DO NOT ADD OR REMOVE ANY IMPORTS FROM THIS FILE͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
import math

# Credits if any͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 1)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 2)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# 3)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

class PriorityQueue(object):
    """
    A queue structure where each element is served in order of priority.
    Elements in the queue are popped based on the priority with higher priority
    elements being served before lower priority elements. If two elements have
    the same priority, they will be served in the order they were added to the
    queue (FIFO).
    """

    def __init__(self):
        """Initialize a new Priority Queue."""
        self.queue = []
        self.counter = 0  # FIFO tracker for tie-breaking

    def append(self, node):
        """
        Append a node to the queue.
        Args:
            node (tuple): Tuple of (priority, node, cost), where `priority` is the total cost (g + h).
        """
        wrapped_node = (node[0], self.counter, node)  # (priority, counter, node)
        self.counter += 1

        # Manual insertion to maintain the order without using sort
        if not self.queue:
            self.queue.append(wrapped_node)
        else:
            inserted = False
            for i in range(len(self.queue)):
                # Compare based on priority first, and then counter for tie-breaking
                if wrapped_node[0] < self.queue[i][0] or (wrapped_node[0] == self.queue[i][0] and wrapped_node[1] < self.queue[i][1]):
                    self.queue.insert(i, wrapped_node)
                    inserted = True
                    break
            if not inserted:
                self.queue.append(wrapped_node)

    def pop(self):
        """
        Pop top priority node from queue.
        Returns:
            The node with the highest priority.
        """
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        return self.queue.pop(0)[2]  # Pop the first element, which is the highest priority

    def top(self):
        """
        Get the top item in the queue.
        Returns:
            The first item stored in the queue (node with the highest priority).
        """
        if self.is_empty():
            raise IndexError("top from an empty priority queue")
        return self.queue[0][2]  # Return the node part of the first element

    def size(self):
        """
        Get the current size of the queue.
        Returns:
            Integer representing the number of items in queue.
        """
        return len(self.queue)

    def is_empty(self):
        """
        Returns True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def __contains__(self, key):
        """
        Containment Check operator for 'in'.
        Args:
            key: The key to check for in the queue.
        Returns:
            True if key is found in queue, False otherwise.
        """
        return any(key == node[2][1] for node in self.queue)

    def __str__(self):
        """Priority Queue to string."""
        return 'PQ:%s' % [node[2] for node in self.queue]

    def clear(self):
        """Reset queue to empty (no nodes)."""
        self.queue = []

    def __iter__(self):
        """Queue iterator."""
        return iter(self.queue)

    def swap(self, a, b):
        """Swaps two nodes in the queue given their indices."""
        self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

    def compare(self, a, b):
        """
        Compare two nodes in queue given their indices.
        Returns:
            True if queue[a] has higher priority (smaller priority value), False otherwise.
        """
        return self.queue[a][0] < self.queue[b][0] or (
            self.queue[a][0] == self.queue[b][0] and self.queue[a][1] < self.queue[b][1])
