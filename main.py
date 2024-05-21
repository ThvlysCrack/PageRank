import pageRank as pr
import GaussSeidelDesc as gs
import dessinecourbe as dc
import recupMat as rm

alg = ['Page Rank classique',
       'Page Rank par Gauss Seidel Descendant']

mat = ['courtois.txt',
       'G10001.txt',
       'india-2004v2.txt',
       'wikipedia-20051105V2.txt']

if __name__ == "__main__":
    
    
    print("Quelle version de Page Rank voulez-vous utiliser ?")
    for i in range(len(alg)):
        print('%d : %s' %(i+1, alg[i]))
    algo = int(input("Veuillez entrer le numéro de la version à appliquer : "))
    
    
    print("Veuillez choisir une matrice parmi les suivantes parmi les suivantes :")
    for i in range(len(mat)):
        print("%d : %s" % (i + 1, mat[i])) 
    matrice = int(input("Veuillez entrer le numéro de la matrice à utiliser : "))
    matrice = mat[matrice-1]
    
    rep = int(input("Combien de simulations voule-vous faire ? : "))
    
    init_alpha = float(input("A combien voulez-vous initialiser le facteur de damping alpha ? : "))
    while (init_alpha < 0 or init_alpha > 1 ):
        init_alpha = float(input("Alpha doit avoir une valeur comprise entre 0 et 1 inclus: "))
    
    fin_alpha = float(input("A quelle valeur de alpha voulez-vous vous arrêter ? : "))
    while (fin_alpha < 0 or fin_alpha > 1 or fin_alpha<=init_alpha):
        init_alpha = float(input("La valeur d'arrêt d'alpha doit avoir une valeur comprise entre 0 et 1 inclus et être inférieure à la valeur d'initialisation: "))
        
    marge = fin_alpha-init_alpha
    pas = marge / rep
    alpha = init_alpha
    iter = []
    temps = []
    csr_mat, zero_rows = csr_mat, zero_rows = rm.buildCSRMatrix(matrice)
    
    for i in range(rep):
        if algo == 1 :
            tp, it  = pr.pageRank(alpha, csr_mat, zero_rows)
        else :
            tp, it  = gs.pageRankGaussSeidelDesc(alpha, csr_mat, zero_rows)
        
        iter.append((alpha,it))
        temps.append((alpha,tp))
        alpha += pas
        print("Simulation %d terminée." %(i+1))
    
    dc.tracer_graph_iter(iter,algo, matrice)
    dc.tracer_graph_temps(temps,algo, matrice)
    
    