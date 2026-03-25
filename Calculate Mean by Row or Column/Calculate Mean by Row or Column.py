def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    
    if mode == 'row':
        for row in matrix:
            means.append(sum(row) / len(row))   # mean of each row
    
    elif mode == 'column':
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        for j in range(num_cols):
            total = sum(matrix[i][j] for i in range(num_rows))
            means.append(total / num_rows)       # mean of each column
    
    return means
