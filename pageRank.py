import numpy as np
import time

def pageRank(alpha, csr_mat, zero_rows):
    nbsom = csr_mat.shape[0]

    # Initialiser rank comme un vecteur colonne et normaliser correctement
    rank = np.random.rand(nbsom, 1)
    rank /= np.sum(rank)
    
    
    e = np.ones((nbsom, 1))
    
    iteration = 0
    zero_rows = np.array(list(zero_rows))
    start_time = time.time()  # Lancement du chrono de convergence
    while True:
        m2 = alpha * csr_mat @ rank  # Calcul principal

        m2 += (1 - alpha) * (e / nbsom)

        zero_sum_contrib = np.sum(rank[zero_rows]) / nbsom
        m2 += zero_sum_contrib * e

        # Vérifier la convergence avec la norme L1
        if np.linalg.norm(m2 - rank, 1) < 1e-6:
            elapsed_time = time.time() - start_time 
            return elapsed_time, iteration

        rank = m2
        iteration += 1
