import matplotlib.pyplot as plt

def tracer_graph_iter(points):
    """
    Cette fonction prend une liste de points (tuples) et crée un graphique
    avec une courbe qui passe par ces points.

    :param points: Liste de tuples (x, y)
    """
    # Séparer les valeurs de la liste en deux listes : x et y
    x = [t[0] for t in points]
    y = [t[1] for t in points]

    # Tracer le graphique
    plt.plot(x, y, marker='o', linestyle='-')

    # Ajouter des étiquettes et un titre
    plt.xlabel('Alpha')
    plt.ylabel('Nombre d itérations')
    plt.title('Nombre d itérations en fonction de alpha')

    # Afficher le graphique
    plt.show()

def tracer_graph_temps(points):
    """
    Cette fonction prend une liste de points (tuples) et crée un graphique
    avec une courbe qui passe par ces points.

    :param points: Liste de tuples (x, y)
    """
    # Séparer les valeurs de la liste en deux listes : x et y
    x = [t[0] for t in points]
    y = [t[1] for t in points]

    # Tracer le graphique
    plt.plot(x, y, marker='o', linestyle='-')

    # Ajouter des étiquettes et un titre
    plt.xlabel('Alpha')
    plt.ylabel('Temps de convergence')
    plt.title('Temps de convergence en fonction de alpha')

    # Afficher le graphique
    plt.show()