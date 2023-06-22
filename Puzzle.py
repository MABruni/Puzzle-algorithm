def solve_puzzle(
        board,
        source,
        destination
    ):
    """
    Finds shortest path from source to destination in a puzzle.

    Args:
        board (list): A 2D array representing the puzzle board. Cells
            that have a # represent blocked paths.
        source (tuple): Coordinates of the starting cell (row, column).
        destination (tuple): Coordinates of the target cell (row, 
            column).
    
    Returns:
        tuple or None: tuple containing a list representing the path 
            from source to destination and a string representing the
            directions taken from source to destination:
            (U = up, D = down, R = right or L = left).
            If no valid path returns None.
    """
    # Creates a list to queue all nodes pending to visit.
    pending_queue = []
    
    # Copies original 2D matrix to store minimum steps for each cell.
    steps_matrix = [
        [float('inf')] * len(board[0]) for row in range(len(board))
    ]
    
    # Sets our starting point in 2D matrix and queue.
    steps_matrix[source[0]][source[1]] = 0
    pending_queue.append(
        (source[0],source[1])
    )

    while pending_queue:
        current_row, current_column = pending_queue.pop(0)

        adjacent_cells = [
            (current_row - 1, current_column),  # Up
            (current_row + 1, current_column),  # Down
            (current_row, current_column + 1),  # Right
            (current_row, current_column - 1)   # Left
        ]

        # Base case, we reached our destination.
        if (current_row, current_column) == destination:
            return solve_puzzle_helper(
                current_row, 
                current_column, 
                source,  
                steps_matrix
            )
        
        # Iterates through all valid neighboring cells
        for adjacent_cell_row, adjacent_cell_column in adjacent_cells:
            if (
                0 <= adjacent_cell_row < len(board) and
                0 <= adjacent_cell_column < len(board[0]) and
                board[adjacent_cell_row][adjacent_cell_column] == '-' and
                steps_matrix[adjacent_cell_row][adjacent_cell_column] >
                steps_matrix[current_row][current_column] + 1
            ):
                # Saves steps to reach a cell from source
                steps_matrix[adjacent_cell_row][adjacent_cell_column] = (
                    steps_matrix[current_row][current_column] + 1
                )

                # Adds neighboring cells to the list
                pending_queue.append(
                    (adjacent_cell_row, adjacent_cell_column)
                )

    # No possible path from source to destination
    return None

def solve_puzzle_helper(
        current_row, 
        current_column, 
        source, 
        matrix
    ):
    """
    Helps find the shortest path from source to destination in a 
    puzzle by backtracking from destination to source using the 
    steps saved in the cells by the main function.

    Args:
        current_row (integer): Row value of the destination cell.
        current_column (integer): Column value of the destination cell.
        source (tuple): Coordinates of the starting cell (row, column).
        matrix (list): 2D array holding the steps needed to reach each
            cell from the source cell.
    
    Returns:
        tuple or None: tuple containing a list representing the path 
            from source to destination and a string representing the
            directions taken from source to destination:
            (U = up, D = down, R = right or L = left).
            If no valid path returns None.
    """

    # Initializes lists to return in our answer.
    result = []
    directions = []

    # Adds our destination cell (starting point for the function)
    result.insert(
        0, 
        (current_row, current_column)
    )

    while True:
        # Base case. Once reached source cell, return
        if (current_row, current_column) == source:
            return (result, ''.join(directions))
        
        adjacent_cells = [
            (current_row - 1, current_column),  # Up
            (current_row + 1, current_column),  # Down
            (current_row, current_column + 1),  # Right
            (current_row, current_column - 1)   # Left
        ]
        
        for adjacent_cell_row, adjacent_cell_column in adjacent_cells:
            # When adjacent cell is closer to source
            if (
                0 <= adjacent_cell_row < len(matrix) and
                0 <= adjacent_cell_column < len(matrix[0]) and
                matrix[adjacent_cell_row][adjacent_cell_column] <
                matrix[current_row][current_column]
            ):

                # Adds cell to result
                result.insert(
                    0, 
                    (adjacent_cell_row, adjacent_cell_column)
                )

                # Checks to add direction to directions
                if adjacent_cell_row != current_row:
                    # Opposite directions because we are backtracking
                    (
                        directions.insert(0, 'D') if    
                        adjacent_cell_row < current_row else 
                        directions.insert(0, 'U')
                    )
                elif adjacent_cell_column != current_column:
                    (
                        directions.insert(0, 'R') if 
                        adjacent_cell_column < current_column else 
                        directions.insert(0, 'L')
                    )
                
                # Sets next cell to explore
                current_row, current_column = (
                    adjacent_cell_row,
                    adjacent_cell_column
                )
                
                break       