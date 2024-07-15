import numpy as np

# 1. Length of a vector


def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum(np.multiply(vector, vector)))
    return len_of_vector

# 2. Dot product


def compute_dot_product(vector1, vector2):
    result = np.sum(np.multiply(vector1, vector2))
    return result

# 3. Multiplying a vector by a matrix


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result


# 4. Multiplying a matrix by a matrix


def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

# 5. Matrix inverse


def inverse_matrix(matrix):
    # Calculate the determinant of the matrix
    det = np.linalg.det(matrix)
    if det == 0:
        return "Matrix is not invertible"
    # Inverse matrix
    a, b = matrix[0, 0], matrix[0, 1]
    c, d = matrix[1, 0], matrix[1, 1]
    result = (1 / det) * np.array([[d, -b], [-c, a]])

    return result
