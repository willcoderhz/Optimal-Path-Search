# coding=utf-8͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

# Author: Raymond Jia͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# Authored: 8/25/2023͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# Last Updated: 8/25/2023 by Raymond Jia͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

import pickle

import matplotlib.pyplot as plt
import networkx


from helpers.explorable_graph import ExplorableGraph
from submission.bfs import breadth_first_search
from submission.ucs import uniform_cost_search
from submission.astar import null_heuristic, euclidean_dist_heuristic, a_star
from submission.bi_ucs import bidirectional_ucs
from submission.bi_astar import bidirectional_a_star
from submission.tri_ucs import tridirectional_search
from submission.tri_astar import tridirectional_upgraded

"""
This file is for visualizing your test cases on the Romania graph. Please scroll to the bottom
to see where you can comment/uncomment different search tests and change the
test case being visualized.
"""

def draw_graph(graph, node_positions=None, start=None, goal=None, path=None, title=''):
  """Visualize results of graph search"""

  explored = [key for key in graph.explored_nodes() if graph.explored_nodes()[key] > 0]

  labels = {}
  for node in graph:
    labels[node] = node
  
  if node_positions is None:
    node_positions = networkx.spring_layout(graph)

  networkx.draw_networkx_nodes(graph, node_positions)
  networkx.draw_networkx_edges(graph, node_positions, style='dashed')
  networkx.draw_networkx_labels(graph, node_positions, labels)

  networkx.draw_networkx_nodes(graph, node_positions, nodelist=explored,
                                node_color='g')
  edge_labels = networkx.get_edge_attributes(graph, 'weight')
  networkx.draw_networkx_edge_labels(graph, node_positions, edge_labels=edge_labels)
  
  if path is not None:
    edges = [(path[i], path[i + 1]) for i in range(0, len(path) - 1)]
    networkx.draw_networkx_edges(graph, node_positions, edgelist=edges,
                                  edge_color='b')

  if start:
    networkx.draw_networkx_nodes(graph, node_positions,
                                  nodelist=[start], node_color='b')

  if goal:
    networkx.draw_networkx_nodes(graph, node_positions,
                                  nodelist=[goal], node_color='y')

  plt.title(title)
  plt.plot()
  plt.show()

def investigate_case(test_name, search_function, goals, **kwargs):
  """
  Visualize student case
  """

  with(open('romania/romania_graph.pickle', 'rb')) as romFile:
    romania = pickle.load(romFile)
  romania = ExplorableGraph(romania)
  romania.reset_search()

  node_positions = {n: romania.nodes[n]['pos'] for n in
                    romania.nodes.keys()}

  path = []
  if len(goals) == 2:
    path = search_function(romania, goals[0], goals[1], **kwargs)
  elif len(goals) == 3:
    if (test_name == "test_tri_ucs_romania"):
      path = search_function(romania, list(goals))
    elif (test_name == "test_tri_upgraded_romania"):
      path = search_function(romania, list(goals), **kwargs)
  
  pos1 = 'o'
  pos2 = 'o'
  if len(path) != 0:
    pos1 = path[0]
    pos2 = path[len(path) - 1]

  print("Your explored nodes: ", romania.explored_nodes())

  draw_graph(romania, node_positions=node_positions,
             start=pos1, goal=pos2, path=path,
             title=test_name + ' blue=start, yellow=goal, green=explored')

# EDIT THE LINE BELOW WITH YOUR GOALS (can be two or three elements)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
goals_to_investigate = ('z', 'b', 'o')

# Uncomment the test you would like to run͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

# BFS͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# investigate_case('test_bfs_romania', breadth_first_search, goals_to_investigate)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

# UCS͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# investigate_case('test_ucs_romania', uniform_cost_search, goals_to_investigate)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

# A* Null Heuristic͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# investigate_case('test_a_star_romania', a_star, goals_to_investigate, heuristic=null_heuristic)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

# A* Euclidean Heuristic͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# investigate_case('test_a_star_romania', a_star, goals_to_investigate, heuristic=euclidean_dist_heuristic)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

# Bi-UCS͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# investigate_case('test_bi_ucs_romania', bidirectional_ucs, goals_to_investigate)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

# Bi-A* Null Heuristic͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# investigate_case('test_bi_a_star_romania', bidirectional_a_star, goals_to_investigate, heuristic=null_heuristic)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

# Bi-A* Euclidean Heuristic͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# investigate_case('test_bi_a_star_romania', bidirectional_a_star, goals_to_investigate, heuristic=euclidean_dist_heuristic)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

# Tri-UCS͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# investigate_case('test_tri_ucs_romania', tridirectional_search, goals_to_investigate)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁

# Tri-Upgraded͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
# investigate_case('test_tri_upgraded_romania', tridirectional_upgraded, goals_to_investigate, heuristic=euclidean_dist_heuristic)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁