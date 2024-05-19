from scipy.sparse import csr_matrix

def buildCSRMatrix(filename):
    rows = []
    cols = []
    data = []

    with open(filename, 'r') as f:
        lines = f.readlines()

    nbSom = int(lines[0].strip())  # Nombre total de sommets
    nbArc = int(lines[1].strip())  # Nombre total d'arcs

    zero_rows = set()

    for line in lines[2:]:
        parts = line.strip().split()
        source = int(parts[0]) - 1  # Numéro du sommet (indexé à partir de 0)
        num_outgoing = int(parts[1])  # Nombre d'arcs sortants

        if num_outgoing == 0:
            zero_rows.add(source)

        index = 2
        for _ in range(num_outgoing):
            destination = int(parts[index]) - 1  # Destination de l'arc
            weight = float(parts[index + 1])     # Poids de l'arc
            rows.append(source)
            cols.append(destination)
            data.append(weight)
            index += 2

    csr_mat = csr_matrix((data, (rows, cols)), shape=(nbSom, nbSom))
    return csr_mat, zero_rows