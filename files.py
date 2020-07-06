import numpy as np


def transition():
    """
    Open the transition Matrix and store it as sparse representation(i, j, k).
    Return the size of the matrix M as well.
    """
    f_transition = open("./data/transition.txt", "r")
    str_transition = f_transition.read()
    f_transition.close()
    np_transition = np.fromstring(str_transition, dtype=int, sep=" ")
    np_transition = np.reshape(np_transition, (-1, 3))  # each row denotes (i, j, k)
    n_matrix = np.max(np_transition)  # size of the matrix
    # E and M are not allocatable because their size are 81433 x 81433 each
    return np_transition, n_matrix


def doctopic():
    """
    Open the doc-topic relationships and store 3 different quantities
    1. 2d array of doc-topic data
    2. How many docs are in each topic
    3. How many topics are there
    """
    f_doctopic = open("./data/doc_topics.txt", "r")
    doc_topic = f_doctopic.read()
    f_doctopic.close()
    np_doc_topic = np.fromstring(doc_topic, dtype=int, sep=" ")
    np_doc_topic = np.reshape(np_doc_topic, (-1, 2))
    np_doc_topic = np_doc_topic[np.argsort(np_doc_topic[:, 1])]
    topic = np.max(np_doc_topic[:, 1])

    n_topic = np.zeros(topic, dtype=int)  # How many docs are in each topic
    for i in range(np_doc_topic.shape[0]):
        t = np_doc_topic[i][1] - 1
        n_topic[t] += 1
    return np_doc_topic, n_topic, topic


def userquery(TSPR):
    """
    Open the distribution file and return it as ndarray
    """
    if TSPR == "PTSPR":
        f_distro = open("./data/user-topic-distro.txt", "r")
    elif TSPR == "QTSPR":
        f_distro = open("./data/query-topic-distro.txt", "r")
    else:
        print("ERR")
        return
    distro = f_distro.read()
    f_distro.close()
    distro = distro.split()
    np_distro = np.asarray(distro)
    np_distro = np.reshape(np_distro, (-1, 14))
    return np_distro


def rq_extractor(queryID, TSPR, topic_pagerank, n_matrix, topic):
    """
    # Extracting rq from Topic_Sensitive_PageRank_Vector
    """
    np_distro = userquery(TSPR)
    user, query = queryID.split("-")
    where = np.intersect1d(np.where(np_distro[:, 0] == user), np.where(np_distro[:, 1] == query))
    where = where[0]

    pq = np_distro[where][2:]
    for i in range(len(pq)):
        pq[i] = pq[i].split(":")[1]

    # Online Computation
    rq = np.zeros(n_matrix)
    pq = np.asarray(pq, dtype=float)
    for t in range(topic):
        rq += pq[t] * topic_pagerank[t]
    return rq
