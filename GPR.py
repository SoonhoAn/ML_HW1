import numpy as np
import time


def GPR(np_transition, n_matrix):
    alpha = 0.2
    # n_links[0] denotes the number of the links from the 1st node
    n_links = np.zeros(n_matrix, dtype=int)
    for i in range(np_transition.shape[0]):
        n = np_transition[i][0] - 1
        n_links[n] += 1

    # Initial PageRank vector
    r = np.random.rand(n_matrix)
    r /= np.sum(r)
    M_vector = (1-alpha)/n_links
    M_vector_emptyrow = (1-alpha)/n_matrix
    alpha_p0 = alpha/n_matrix

    iteration = 0
    while True:
        iteration += 1
        r_new = np.zeros(n_matrix)
        for x in range(np_transition.shape[0]):
            i = np_transition[x][0] - 1
            j = np_transition[x][1] - 1
            r_new[j] += M_vector[i] * r[i]
            # r_new[j] += (1 - alpha) * (1.0 / n_links[i]) * r[i]
        for x in range(n_matrix):
            if n_links[x] == 0:
                r_new += M_vector_emptyrow * r[x]
                # r_new += (1 - alpha) * r[x] / n_matrix
        r_new += alpha_p0
        # r_new += 0.2 * (1.0 / n_matrix)
        error = np.linalg.norm(r_new - r, ord=1)
        print("\rIteration : %d, error : %.9f" % (iteration, error), end=" ")
        r = r_new
        if error < 10**(-8):
            break
    return r
