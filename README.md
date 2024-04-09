# Shortest Path Puzzle Solver
This Python script was developed as part of a final project for CS162. It finds the shortest path from a source to a destination in a puzzle using a Breadth-First Search (BFS) algorithm.

To run the script, save it in a file (e.g., puzzle.py) and run it from the terminal using `python3 puzzle.py`. The script won't execute on its own, you need to include the desired arguments at the end of the file and call the function. One example to test it could be:
```
board = [
    ['-', '-', '-', '#', '-', '-', '-'],
    ['-', '#', '-', '#', '-', '#', '-'],
    ['-', '#', '-', '#', '-', '#', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
]
source = (0, 0)
destination = (3, 6)

print(solve_puzzle(board, source, destination))
```

# Key Concepts
## Breadth-First Search (BFS)
This algorithm is a traversing or searching tree (or graph) data structure. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a ‘search key’) and explores the neighbor nodes at the present depth prior to moving on to nodes at the next depth level.
## Queue Data Structure
In BFS, a queue data structure is used. It is a FIFO (First-in, first-out) data structure that stores and retrieves items in the order they were added.
## 2D Matrix Representation
The puzzle board is represented as a 2D matrix where each cell represents a possible path or a blocked path.
## Backtracking
Once the destination is reached, the algorithm backtracks from the destination cell to the source cell to find the shortest path.

# Algorithm Explanation
The solve_puzzle function takes a 2D board, a source cell, and a destination cell as input. It uses BFS to find the shortest path from the source to the destination. It maintains a queue of cells to visit and a 2D matrix to store the minimum steps needed to reach each cell from the source.

The solve_puzzle_helper function is used to backtrack from the destination cell to the source cell using the steps stored in the 2D matrix. It returns the shortest path and the directions taken from the source to the destination.


# Key Achievements
## Understanding and Implementing BFS
One of the major achievements was understanding the Breadth-First Search (BFS) algorithm and successfully implementing it to solve the puzzle. This was a significant step in improving my knowledge of graph theory and traversal algorithms.
## Working with 2D Matrices
The puzzle was represented as a 2D matrix, which required me to effectively manipulate and traverse 2D data structures. This improved my understanding of how to work with complex data structures.
## Implementing Backtracking
Implementing the backtracking process to find the shortest path from the destination to the source was a challenging but rewarding experience. It not only helped me understand the concept of backtracking but also its practical application.
## Problem-Solving Skills
The process of breaking down the problem, figuring out the logic, and writing the code to solve the puzzle was a great exercise in problem-solving and critical thinking.


# Learnings
## Importance of Choosing the Right Algorithm
The experience reinforced the importance of choosing the right algorithm for the problem at hand. BFS was the right choice for this problem as it guarantees the shortest path in an unweighted graph.
## Debugging and Testing
Debugging the code when it didn’t work as expected and testing it with different inputs taught me the importance of thorough testing and debugging in programming.
## Code Optimization
I learned how to optimize the code to make it more efficient. For example, using a queue data structure for BFS helped in achieving a time complexity of O(V+E).
## Documentation and Code Readability
Writing clear comments and maintaining a well-documented codebase is crucial. It not only helps others understand your code but also aids in debugging and future enhancements.
