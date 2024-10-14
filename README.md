# Optimal Path Search Algorithm Implementation

This project implements several classic search algorithms to solve pathfinding problems, focusing on calculating the optimal route between two points on a map of Romania. Search algorithms are widely used in artificial intelligence for problem-solving where solutions aren't immediately clear. The goal of this project is to compute the most efficient path while minimizing time and space costs.

The project utilizes an undirected graph to represent the map of Romania, with an optional Atlanta graph available for a race mode. You can choose from different algorithms such as Depth-First Search, Breadth-First Search, and A* to explore and find the optimal path between two locations.

## Table of Contents
- [Setup](#setup)
- [Dependencies](#dependencies)
- [Jupyter Notebook](#jupyter-notebook)
- [Tips for Jupyter](#tips-for-jupyter)
- [Testing](#testing)
- [Visualization](#visualization)

## Setup

To get started, create and activate a Conda environment. Run the following commands:

```bash
conda create --name optimal_path_env python=3.9 -y
conda activate optimal_path_env

If you used a different environment name, you can list all environments with conda env list and ensure the correct one is activated.

Dependencies
After activating your environment, install the required dependencies:

pip install -r requirements.txt

Jupyter Notebook
To run the project in a Jupyter Notebook, execute:

jupyter notebook

This will open the notebook.ipynb file in your browser. If it doesn't open automatically, access it via http://localhost:8888.

Tips for Jupyter
Here are some troubleshooting tips when using Jupyter:

Kernel not starting: Ensure your virtual environment is activated before starting the notebook (conda activate optimal_path_env).
Cell execution issues: Ensure dependent cells are run in the correct order. Use the "Run All" command if needed to execute everything sequentially.
Unexpected variable values: Check if cells that modify variables were rerun unintentionally. Running cells in the wrong order can alter the flow of the program.
Testing
There are custom tests provided to validate the functionality of your implementation:

search_basic_tests.py: Runs basic tests and visualizes the Romania graph.
search_romania_tests.py: Comprehensive tests for the Romania graph.
search_atlanta_tests.py: Tests for the optional Atlanta graph.

## To run a test, use:

python search_romania_tests.py

## For a specific test:

python search_romania_tests.py SearchRomaniaTests.test_bfs_romania

## Visualization

The project includes visualization tools to help you better understand the search process on the Romania and Atlanta graphs. You can visualize the graph and the path explored by running the provided tests, making it easier to debug and analyze algorithm performance.

