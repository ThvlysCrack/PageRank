import numpy as np
import time
import recupMat

def pageRankGaussSeidelDesc(alpha, filename):
    csr_mat, zero_rows = recupMat.buildCSRMatrix(filename)
    nbsom = csr_mat.shape[0]

    # Initialiser le vecteur rank avec des valeurs uniformes
    rank = np.random.rand(nbsom,1)
    rank/=np.linalg.norm(rank,1)
    e = np.ones((nbsom, 1)) / nbsom
    rank_new = np.zeros_like(rank)
    iteration = 0
    start_time = time.time()
    while True:
        for i in range(nbsom - 1, -1, -1):
            row_start = csr_mat.indptr[i]
            row_end = csr_mat.indptr[i + 1]
            row_data = csr_mat.data[row_start:row_end]
            row_indices = csr_mat.indices[row_start:row_end]

            rank_sum = np.dot(row_data, rank[row_indices])
            rank_new[i] = alpha * rank_sum + (1 - alpha) * e[i]

        # Ajouter la contribution des lignes sans arcs sortants
        zero_sum_contrib = np.sum(rank[list(zero_rows)]) / nbsom
        rank_new += alpha * zero_sum_contrib * e

        if np.linalg.norm(rank_new - rank, 1) < 1e-6:
            elapsed_time = time.time() - start_time
            return elapsed_time, iteration

        rank = rank_new.copy()
        iteration += 1

