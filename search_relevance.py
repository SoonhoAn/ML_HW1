import os
import numpy as np


def main():
    print("test")
    directory = "./data/indri-lists"
    files = os.listdir(directory)
    f_eval = open("./data_out/eval.txt", "w")

    for file in files:
        f_indri = open(directory + "/" + file, "r")
        queryID = file.split(".")[0]
        indri = f_indri.read()
        f_indri.close()
        indri = indri.split()
        np_indri = np.asarray(indri)
        np_indri = np.reshape(np_indri, (-1, 6))
        np_indri[:, 0] = queryID
        # f_trec = open("./data_out/"+file, "w")
        # np.savetxt(f_trec, np_indri[:, :], fmt="%s", delimiter=" ")
        # f_trec.close()
        np.savetxt(f_eval, np_indri[:, :], fmt="%s", delimiter=" ")
        print("pause")
    f_eval.close()




    print("stop")


if __name__ == "__main__":
    main()
