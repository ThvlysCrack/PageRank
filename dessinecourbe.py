import matplotlib.pyplot as plt

def tracer_graph_iter(points, algo, matrice):
    """
    Cette fonction prend une liste de points (tuples) et crée un graphique
    avec une courbe qui passe par ces points.

    :param points: Liste de tuples (x, y)
    :param algo: Entier qui indique l'algorithme utilisé (1 ou 2)
    """
    # Séparer les valeurs de la liste en deux listes : x et y
    x = [t[0] for t in points]
    y = [t[1] for t in points]
    
    matrice = matrice.split('.')[0]

    # Tracer le graphique
    plt.plot(x, y, marker='o', linestyle='-')

    # Ajouter des étiquettes et un titre
    plt.xlabel('Alpha')
    plt.ylabel('Nombre d\'itérations')
    plt.title('Nombre d\'itérations en fonction de alpha')

    # Déterminer le nom de l'algorithme
    algo_name = 'PageRankClassique' if algo == 1 else 'Gauss Seidel Descendant'

    # Construire le nom du fichier
    filename = f"graphique/{algo_name}_{matrice}_Iterations_{len(points)}.png"

    # Sauvegarder le graphique en PNG
    plt.savefig(filename)

    # Afficher le graphique
    plt.show()

def tracer_graph_temps(points, algo, matrice):
    """
    Cette fonction prend une liste de points (tuples) et crée un graphique
    avec une courbe qui passe par ces points.

    :param points: Liste de tuples (x, y)
    :param algo: Entier qui indique l'algorithme utilisé (1 ou 2)
    """
    # Séparer les valeurs de la liste en deux listes : x et y
    x = [t[0] for t in points]
    y = [t[1] for t in points]
    
    matrice = matrice.split('.')[0]

    # Tracer le graphique
    plt.plot(x, y, marker='o', linestyle='-')

    # Ajouter des étiquettes et un titre
    plt.xlabel('Alpha')
    plt.ylabel('Temps de convergence')
    plt.title('Temps de convergence en fonction de alpha')

    # Déterminer le nom de l'algorithme
    algo_name = 'PageRankClassique' if algo == 1 else 'Gauss Seidel Descendant'

    # Construire le nom du fichier
    filename = f"graphique/{algo_name}__{matrice}_Temps_{len(points)}.png"

    # Sauvegarder le graphique en PNG
    plt.savefig(filename)

    # Afficher le graphique
    plt.show()
