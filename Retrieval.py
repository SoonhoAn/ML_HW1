import os
from files import *


def TSPR_Retrieval(retrieval, TSPR, f_eval, r_TSPR, n_matrix, topic):
    """
    This function includes "Online Computation" of TSPR.
    With TSPR, this function retrieves the scores based on Weighted Sum Method.
    """
    PR_weight, indri_weight = (0, 0)
    if retrieval == "NS":
        PR_weight, indri_weight = (1, 0)
    elif retrieval == "WS":
        PR_weight, indri_weight = (100, 1)
    elif retrieval == "CM":
        PR_weight, indri_weight = (1, 1)

    directory = "./data/indri-lists"
    files = os.listdir(directory)
    np_distro = userquery(TSPR)
    for u in range(np_distro.shape[0]):
        f_indri = open(directory + "/" + files[u], "r")
        queryID = files[u].split(".")[0]
        indri = f_indri.read()
        f_indri.close()
        indri = indri.split()
        np_indri = np.asarray(indri)
        np_indri = np.reshape(np_indri, (-1, 6))
        np_indri[:, 0] = queryID
        rq = rq_extractor(queryID, TSPR, r_TSPR, n_matrix, topic)
        score = np_indri[:, 4].astype('float64')
        score /= -np.sum(score)

        for i in range(np_indri.shape[0]):
            docnum = int(np_indri[i][2])
            np_indri[i][4] = format(indri_weight * score[i] + PR_weight * rq[docnum - 1], ".9f")
        np_indri = np_indri[np.argsort(np_indri[:, 4])]
        for i in range(np_indri.shape[0]):
            np_indri[i][3] = "%d" % (i + 1)
        np.savetxt(f_eval, np_indri[:, :], fmt="%s", delimiter=" ")


def GPR_Retrieval(retrieval, f_eval, r):
    PR_weight, indri_weight = (0, 0)
    if retrieval == "NS":
        PR_weight, indri_weight = (1, 0)
    elif retrieval == "WS":
        PR_weight, indri_weight = (100, 1)
    elif retrieval == "CM":
        PR_weight, indri_weight = (1, 1)

    directory = "./data/indri-lists"
    files = os.listdir(directory)
    for u in range(len(files)):
        f_indri = open(directory + "/" + files[u], "r")
        queryID = files[u].split(".")[0]
        indri = f_indri.read()
        f_indri.close()
        indri = indri.split()
        np_indri = np.asarray(indri)
        np_indri = np.reshape(np_indri, (-1, 6))
        np_indri[:, 0] = queryID

        score = np_indri[:, 4].astype('float64')
        score /= -np.sum(score)

        for i in range(np_indri.shape[0]):
            docnum = int(np_indri[i][2])
            np_indri[i][4] = format(indri_weight * score[i] + PR_weight * r[docnum - 1], ".9f")
        np_indri = np_indri[np.argsort(np_indri[:, 4])]
        for i in range(np_indri.shape[0]):
            np_indri[i][3] = "%d" % (i + 1)
        np.savetxt(f_eval, np_indri[:, :], fmt="%s", delimiter=" ")


"""
Functions below are for the NS without indri-list information.
From the Question @26 in Piazza, TA originally answered that
"For NS, you really shouldn't use any information from 'indri-list'"
so I implemented this code, but later TA corrected the answer
and now the code below is useless.
"""
'''
def TSPR_NS(TSPR, f_eval, r_TSPR, n_matrix, topic):
    """
    This function includes "Online Computation" of TSPR.
    With TSPR, this function retrieves the scores based on No Search Method.
    """
    num_top = 500
    np_distro = userquery(TSPR)
    for u in range(np_distro.shape[0]):
        pq = np_distro[u][2:]
        user, query = np_distro[u][:2]
        for i in range(len(pq)):
            pq[i] = pq[i].split(":")[1]

        # Online Computation
        rq = np.zeros(n_matrix)
        pq = np.asarray(pq, dtype=float)
        for t in range(topic):
            rq += pq[t] * r_TSPR[t]

        top_500 = np.argsort(rq)
        list_eval = []
        for i in range(num_top):
            list_eval.append("%s-%s" % (user, query))
            list_eval.append("Q0")
            list_eval.append(top_500[-1 - i])
            list_eval.append(i+1)
            list_eval.append(format(rq[top_500[-1 - i]], ".9f"))
            list_eval.append("%s_NS" % TSPR)
        np_eval = np.asarray(list_eval)
        np_eval = np.reshape(np_eval, (-1, 6))
        np.savetxt(f_eval, np_eval[:, :], fmt="%s", delimiter=" ")


def GPR_NS(f_eval, r):
    num_top = 500
    top_500 = np.argsort(r)
    np_distro = userquery("PTSPR")  # just to get the queryID
    for u in range(np_distro.shape[0]):
        user, query = np_distro[u][:2]
        list_eval = []
        for i in range(num_top):
            list_eval.append("%s-%s" % (user, query))
            list_eval.append("Q0")
            list_eval.append(top_500[-1 - i])
            list_eval.append(i+1)
            list_eval.append(format(r[top_500[-1 - i]], ".9f"))
            list_eval.append("GPR_NS")
        np_eval = np.asarray(list_eval)
        np_eval = np.reshape(np_eval, (-1, 6))
        np.savetxt(f_eval, np_eval[:, :], fmt="%s", delimiter=" ")
'''
