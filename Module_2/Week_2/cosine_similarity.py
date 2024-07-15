import numpy as np
from basic_operations import compute_vector_length, compute_dot_product


def compute_cosine(v1, v2):
    product = compute_dot_product(v1, v2)
    len1 = compute_vector_length(v1)
    len2 = compute_vector_length(v2)
    cos_sim = product/(len1*len2)
    return cos_sim
