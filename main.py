from GPR import *
from TSPR import *
from Retrieval import *


def main():
    folder_route = "./"
    QTSPR, PTSPR = ("QTSPR", "PTSPR")
    NS, WS, CM = ("NS", "WS", "CM")

    t1 = time.time()
    np_transition, n_matrix = transition()
    r_GPR = GPR(np_transition, n_matrix)
    t2 = time.time() - t1
    print("\nTime taken for PageRank Computation : %f seconds" % t2)

    f_sample = open("%sGPR.txt" % folder_route, "w")
    for i in range(n_matrix):
        f_sample.write("%d %.9f\n" % ((i+1), r_GPR[i]))
    f_sample.close()

    t1 = time.time()
    np_doc_topic, n_topic, topic = doctopic()
    r_TSPR = TSPR(np_transition, n_matrix, np_doc_topic, n_topic, topic)
    t2 = time.time() - t1
    print("\nTime taken for TopicSensitivePageRank Computation : %f seconds" % t2)

    sample_queryID = "2-1"
    rq_ptsqr_sample = rq_extractor(sample_queryID, PTSPR, r_TSPR, n_matrix, topic)
    rq_qtsqr_sample = rq_extractor(sample_queryID, QTSPR, r_TSPR, n_matrix, topic)
    user, query = sample_queryID.split("-")
    f_sample = open("%s%s-U%sQ%s.txt" % (folder_route, PTSPR, user, query), "w")
    for i in range(n_matrix):
        f_sample.write("%d %.9f\n" % ((i + 1), rq_ptsqr_sample[i]))
    f_sample.close()
    f_sample = open("%s%s-U%sQ%s.txt" % (folder_route, QTSPR, user, query), "w")
    for i in range(n_matrix):
        f_sample.write("%d %.9f\n" % ((i + 1), rq_qtsqr_sample[i]))
    f_sample.close()

    """
    f_sample = open("%sTSPR.txt" % folder_route, "w")
    for t in range(topic):
        for i in range(n_matrix):
            f_sample.write("%d %.9f\n" % ((i + 1), r_TSPR[t][i]))
    f_sample.close()
    """

    # GPR-NS
    t1 = time.time()
    f_GPR_NS = open("%sGPR_NS.txt" % folder_route, "w")
    GPR_Retrieval(NS, f_GPR_NS, r_GPR)
    f_GPR_NS.close()
    t2 = time.time() - t1
    print("Time taken for retriving GPR-NS : %f seconds" % t2)

    # GPR-WS
    t1 = time.time()
    f_GPR_WS = open("%sGPR_WS.txt" % folder_route, "w")
    GPR_Retrieval(WS, f_GPR_WS, r_GPR)
    f_GPR_WS.close()
    t2 = time.time() - t1
    print("Time taken for retriving GPR-WS : %f seconds" % t2)

    # GPR-CM
    t1 = time.time()
    f_GPR_CM = open("%sGPR_CM.txt" % folder_route, "w")
    GPR_Retrieval(CM, f_GPR_CM, r_GPR)
    f_GPR_CM.close()
    t2 = time.time() - t1
    print("Time taken for retriving GPR-CM : %f seconds" % t2)

    # QTSPR-NS
    t1 = time.time()
    f_QTSPR_NS = open("%s%s-NS" % (folder_route, QTSPR), "w")
    TSPR_Retrieval(NS, QTSPR, f_QTSPR_NS, r_TSPR, n_matrix, topic)
    f_QTSPR_NS.close()
    t2 = time.time() - t1
    print("Time taken for retriving QTSPR-NS : %f seconds" % t2)

    # QTSPR-WS
    t1 = time.time()
    f_QTSPR_WS = open("%s%s-WS.txt" % (folder_route, QTSPR), "w")
    TSPR_Retrieval(WS, QTSPR, f_QTSPR_WS, r_TSPR, n_matrix, topic)
    f_QTSPR_WS.close()
    t2 = time.time() - t1
    print("Time taken for retriving QTSPR-WS : %f seconds" % t2)

    # QTSPR-CM
    t1 = time.time()
    f_QTSPR_CM = open("%s%s-CM.txt" % (folder_route, QTSPR), "w")
    TSPR_Retrieval(CM, QTSPR, f_QTSPR_CM, r_TSPR, n_matrix, topic)
    f_QTSPR_CM.close()
    t2 = time.time() - t1
    print("Time taken for retriving QTSPR-CM : %f seconds" % t2)

    # PTSPR-NS
    t1 = time.time()
    f_PTSPR_NS = open("%s%s-NS" % (folder_route, PTSPR), "w")
    TSPR_Retrieval(NS, PTSPR, f_PTSPR_NS, r_TSPR, n_matrix, topic)
    f_PTSPR_NS.close()
    t2 = time.time() - t1
    print("Time taken for retriving PTSPR-NS : %f seconds" % t2)

    # PTSPR-WS
    t1 = time.time()
    f_PTSPR_WS = open("%s%s-WS.txt" % (folder_route, PTSPR), "w")
    TSPR_Retrieval(WS, PTSPR, f_PTSPR_WS, r_TSPR, n_matrix, topic)
    f_PTSPR_WS.close()
    t2 = time.time() - t1
    print("Time taken for retriving PTSPR-WS : %f seconds" % t2)

    # PTSPR-CM
    t1 = time.time()
    f_PTSPR_CM = open("%s%s-CM.txt" % (folder_route, PTSPR), "w")
    TSPR_Retrieval(CM, PTSPR, f_PTSPR_CM, r_TSPR, n_matrix, topic)
    f_PTSPR_CM.close()
    t2 = time.time() - t1
    print("Time taken for retriving PTSPR-CM : %f seconds" % t2)


if __name__ == '__main__':
    main()
