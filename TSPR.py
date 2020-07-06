import time
import numpy as np


def TSPR(np_transition, n_matrix, np_doc_topic, n_topic, topic):
    alpha = 0.8
    beta = 0.1
    gamma = 0.1
    # n_links[0] denotes the number of the links from the 1st node
    n_links = np.zeros(n_matrix, dtype=int)
    for i in range(np_transition.shape[0]):
        n = np_transition[i][0] - 1
        n_links[n] += 1
    # Initial TopicSensitivePageRank vector(matrix)
    r = np.random.rand(topic, n_matrix)
    for i in range(topic):
        r[i] /= np.sum(r[i])
    # Offline Computation
    M_vector = alpha/n_links
    M_vector_emptyrow = alpha / n_matrix
    beta_pt = beta/n_topic
    gamma_p0 = gamma/n_matrix
    for t in range(topic):
        iteration = 0
        offset = np.sum(n_topic[0:t])
        while True:
            iteration += 1
            r_new = np.zeros(n_matrix)
            for x in range(np_transition.shape[0]):
                i = np_transition[x][0] - 1
                j = np_transition[x][1] - 1
                r_new[j] += M_vector[i] * r[t][i]
            for x in range(n_matrix):
                if n_links[x] == 0:
                    r_new += M_vector_emptyrow * r[t][x]
            for x in range(n_topic[t]):
                i = np_doc_topic[x+offset][0] - 1
                j = np_doc_topic[x+offset][1] - 1
                if j != t:
                    print("err j:%d, t:%d", j, t)
                    break
                r_new[i] += beta_pt[t]
            r_new += gamma_p0
            error = np.linalg.norm(r_new - r[t], ord=1)
            print("\rTopic : %d, Iteration : %d, error : %.9f" % (t+1, iteration, error), end=" ")
            r[t] = r_new
            if error < 10 ** (-8):
                break
    return r
