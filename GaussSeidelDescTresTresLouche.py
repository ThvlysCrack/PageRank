import numpy as np
import time
import recupMat

csr_mat, zero_rows = recupMat.buildCSRMatrix('wikipedia-20051105V2.txt')

def pageRankGaussSeidelDesc(alpha, csr_mat, zero_rows):
    nbsom = csr_mat.shape[0]

    rank = np.random.rand(nbsom,1)
    rank/=np.linalg.norm(rank,1)
    e = np.ones((nbsom, 1)) / nbsom
    rank_new = np.zeros_like(rank)
    iteration = 0
    start_time = time.time()
    tour = nbsom -1
    instant = tour
    while True:
        #très très louche mais rapide impossible demander au prof
        instant %= 8
        row_start = csr_mat.indptr[instant]
        row_end = csr_mat.indptr[instant+1]
        row_data = csr_mat.data[row_start:row_end]
        row_indices = csr_mat.indices[row_start:row_end]
        rank_sum = np.dot(row_data, rank[row_indices])
        rank_new[instant] = alpha * rank_sum + (1 - alpha) * e[instant]
        

        zero_sum_contrib = np.sum(rank[list(zero_rows)]) / nbsom
        rank_new += alpha * zero_sum_contrib * e

        if np.linalg.norm(rank_new - rank, 1) < 1e-6:
            elapsed_time = time.time() - start_time
            return elapsed_time, iteration, rank

        rank = rank_new.copy()
        iteration += 1
        instant -=1

print("courtois.txt".split('.')[0])