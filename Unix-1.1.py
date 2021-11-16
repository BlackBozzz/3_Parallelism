import multiprocessing
from multiprocessing import Process, Pool


def element(index, A, B, conn):
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    conn.send(res)


if __name__ == '__main__':
    with open("matrix1", "r") as file:
        matrix1 = [[int(number) for number in line.split()] for line in file.read().splitlines()]

    with open("matrix2", "r") as file:
        matrix2 = [[int(number) for number in line.split()] for line in file.read().splitlines()]



    log = open("log", "w")

    res_marrix = []
    for i, dex in enumerate(range(len(matrix1))):
        res_marrix.append([])
        for k in range(len(matrix2[0])):
            res_marrix[i].append(0)
            p_conn, c_conn = multiprocessing.Pipe()
            Process(target = element, args = ((i, k), matrix1, matrix2, c_conn)).start()
            Var = p_conn.recv()
            log.write(f"{i} {k} {Var}\n")

    log.close()

    with open("log", "r") as log:
        for index in log.readlines():
            line, column, Var = index.split()
            res_marrix[int(line)][int(column)] = str(Var)

    with open("result", "w") as file:
        for line in res_marrix:
            file.write(" ".join(line)+"\n")


    log.close()
