import pageRank as pr
import GaussSeidelDesc as gs
import dessinecourbe as dc

alg = ['Page Rank classique',
       'Page Rank par Gauss Seidel Descendant']

mat = ['courtois.txt',
       'G10001.txt',
       'india-2004v2.txt',
       'wikipédia-20051105V2.txt']

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
    init_alpha = 1/rep
    alpha = init_alpha
    iter = []
    temps = []
    
    for i in range(rep):
        if algo == 1 :
            tp, it  = pr.pageRank(alpha, matrice)
        else :
            tp, it  = gs.pageRankGaussSeidelDesc(alpha, matrice)
        
        iter.append((alpha,it))
        temps.append((alpha,tp))
        alpha += init_alpha
        print("Simulation %d terminée." %(i+1))
    
    print(iter)
    print(temps)
    dc.tracer_graph_iter(iter)
    dc.tracer_graph_temps(temps)
    
    