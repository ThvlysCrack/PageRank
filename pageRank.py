import numpy as np
import time

def pageRank(alpha, csr_mat, zero_rows):
    
    nbsom = csr_mat.shape[0]

    rank = np.random.rand(nbsom, 1)
    rank /= np.sum(rank)  # Normaliser correctement le vecteur rank

    e = np.ones((nbsom, 1))
    
    iteration = 0
    start_time = time.time()  #Lancement du chrono de convergence

    while True:
        m2 = alpha * csr_mat @ rank 

        
        m2 += (1 - alpha) * (e / nbsom)

        
        zero_sum_contrib = np.sum(rank[list(zero_rows)]) / nbsom
        m2 += zero_sum_contrib * e

        if np.linalg.norm(m2 - rank, 1) < 1e-6:
            elapsed_time = time.time() - start_time 
            return elapsed_time, iteration

        rank = m2
        iteration += 1



