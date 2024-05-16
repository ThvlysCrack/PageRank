import numpy as np
import time
from scipy.sparse import csr_matrix, diags

def buildCSRMatrix(filename):
    rows = []
    cols = []
    data = []

    with open(filename, 'r') as f:
        lines = f.readlines()

    nbSom = int(lines[0].strip())  # Nombre total de sommets
    nbArc = int(lines[1].strip())  # Nombre total d'arcs

    # Traitement des lignes décrivant les arcs sortants pour chaque sommet
    for line in lines[2:]:
        parts = line.strip().split()
        source = int(parts[0]) - 1  # Numéro du sommet (indexé à partir de 0)
        num_outgoing = int(parts[1])  # Nombre d'arcs sortants

        # Parcours des paires de destinations et de poids
        index = 2
        for _ in range(num_outgoing):
            destination = int(parts[index]) - 1  # Destination de l'arc
            weight = float(parts[index + 1])     # Poids de l'arc
            rows.append(source)
            cols.append(destination)
            data.append(weight)
            index += 2

    # Construction de la matrice CSR
    csr_mat = csr_matrix((data, (rows, cols)), shape=(nbSom, nbSom))
    return csr_mat

def pageRank(csr_mat, alpha, epsilon=1e-6):
    nbsom = csr_mat.shape[0]

    rank = np.random.rand(nbsom, 1)
    rank /= np.linalg.norm(rank, 1)

    # Construction de la matrice G
    D = np.full((nbsom,), (1 - alpha) / nbsom)
    D_full = diags(D, 0, format='csr')  # Utilisation de diags pour construire D_full en format CSR
    G = alpha * csr_mat + D_full

    iteration = 0
    start_time = time.time()  # Mesurer le temps de début

    while True:
        m2 = G @ rank
        if np.linalg.norm(m2 - rank, 1) < epsilon:
            elapsed_time = time.time() - start_time  # Calculer le temps écoulé
            print(f"Le programme a convergé en {iteration} itérations.")
            print(f"Temps d'exécution : {elapsed_time:.4f} secondes.")
            return rank
        
        # Mise à jour du rang
        rank = m2
        iteration += 1

# Exemple d'utilisation
#filename = './wikipedia-20051105v2.txt'
filename = './india-2004v2.txt'
csr_mat = buildCSRMatrix(filename)
resultat = pageRank(csr_mat, alpha=0.85)
