import numpy as np
import time
import recupMat

def pageRank(alpha, filename):
    csr_mat, zero_rows = recupMat.buildCSRMatrix(filename)
    nbsom = csr_mat.shape[0]

    rank = np.ones((nbsom, 1)) / nbsom
    e = np.ones((nbsom, 1))
    
    iteration = 0
    start_time = time.time()  # Mesurer le temps de début

    while True:
        m2 = alpha * csr_mat @ rank 

        # Ajouter le terme de téléportation directement
        m2 += (1 - alpha) * (e / nbsom)

        # Ajouter la contribution des lignes sans arcs sortants
        zero_sum_contrib = np.sum(rank[list(zero_rows)]) / nbsom
        m2 += zero_sum_contrib * e

        if np.linalg.norm(m2 - rank, 1) < 1e-6:
            elapsed_time = time.time() - start_time 
            return elapsed_time, iteration

        rank = m2
        iteration += 1



