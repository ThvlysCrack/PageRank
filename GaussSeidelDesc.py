import numpy as np
import time


def pageRankGaussSeidelDesc(alpha, csr_mat):
    epsilon = 1e-6
    n = csr_mat.shape[0]
    

    pagerank = np.ones(n) / n
    
    # Calculer le nombre de liens sortants pour chaque page
    out_degree = np.array(csr_mat.sum(axis=1)).flatten()
    
    # Identifier les pages dangling
    dangling_pages = np.where(out_degree == 0)[0]
    
    start_time = time.time()
    iteration = 0
    while True:
        prev_pagerank = pagerank.copy()
        
        # Calculer la somme des contributions des pages qui pointent vers chaque page
        rank_sum = alpha * csr_mat.transpose().dot(prev_pagerank / np.maximum(out_degree, 1))
        
        # Ajouter la contribution des pages dangling
        dangling_contribution = (1 - alpha) * np.sum(prev_pagerank[dangling_pages]) / n
        rank_sum += dangling_contribution
        
        # Mettre à jour le vecteur PageRank
        pagerank = rank_sum
        
        if np.linalg.norm(pagerank - prev_pagerank, 1) < epsilon:
            elapsed_time = time.time() - start_time 
            return elapsed_time, iteration
        iteration += 1
    

        