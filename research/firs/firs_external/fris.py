import numpy as np
import dataFris
import matplotlib.pyplot as plt

def euclidean(x,y):
    return np.sqrt(np.sum((x-y)**2))

EPS = 1e-5
def S(u,x,xp,ro):
    return (ro(u,xp) - ro(u,x)) / (ro(u,xp) + ro(u,x) + EPS)

def diff(a,b):
    # 5 -> {5}
    a = np.atleast_1d(a)
    b = np.atleast_1d(b)
    #diffeer two sets
    return np.setdiff1d(a,b)

def union(a,b):
    a = np.atleast_1d(a)
    b = np.atleast_1d(b)
    return np.union1d(a,b)

#work with indexes always
class FRiSSTOLP:
    def __init__(self,Xl,y,ro,alpha=0.75,theta=0):
        self.Xl = Xl
        self.y = y
        self.ro = ro
        self.alpha = alpha
        self.theta = theta

    #returns closet element (it's index) to u from U
    #U - index array
    def NN(self,u,U):
        print(u)
        Xl = self.Xl
        n = U.size
        best = -1
        val = 0
        for i in range(n):
            cur = self.ro(u,Xl[U[i]])
            if best == -1 or cur < val:
                val = cur
                best = i
        return U[best]

    def without(self, U):
        l = self.Xl.shape[0] #dimension
        others = diff(np.arange(l),U)
        return others

    #returns new etalon to class Y
    #Xy - index array
    def FindEtalon(self,Xy,Omega):
        if Xy.size == 1: return Xy[0]

        n = Xy.size
        Xl = self.Xl

        Dx = np.zeros(n)
        Tx = np.zeros(n)

        print("I do Dx")
        # calculate Dx
        for x in range(n):
            for u in range(n):
                if u == x: continue
                closest = self.NN(Xl[Xy[u]],Omega)
                Dx[x] += S(Xl[Xy[u]],Xl[Xy[x]],Xl[closest],self.ro)
        Dx = Dx / (n-1)
        print()

        print("I do Tx")
        # calculate Tx
        others = self.without(Xy)
        m = others.size
        for x in range(n):
            for v in range(m):
                closest = self.NN(Xl[others[v]],Omega)
                Tx[x] += S(Xl[others[v]], Xl[Xy[x]], Xl[closest],self.ro)
        Tx = Tx / m

        Ex = self.alpha * Dx + (1-self.alpha) * Tx
        best = np.argmax(Ex)
        # {index} returns
        return np.atleast_1d(Xy[best])

    def Main(self):
        print("Main")
        l = self.Xl.shape[0] #dim
        Xl = self.Xl
        #classes - it's cnt
        #max + 1, if classes named 0...n-1
        classes = int(np.amax(self.y)+1)

        #create vectors with elements
        X = []
        for i in range(classes):
            X.append(np.arange(l)[self.y==i])

        #get first etalon from each class
        # step 1
        Omega0y = []
        for i in range(classes):
            etalon = self.FindEtalon(X[i],self.without(X[i]))
            Omega0y.append(etalon)

        print(Omega0y)

        #union that etalons to Omega0
        Omega0 = Omega0y[0]
        for i in range(1,classes):
            Omega0 = union(Omega0, Omega0y[i])

        print(Omega0)

        # step2
        Omega = []
        for i in range(classes):
            etalon = self.FindEtalon(X[i], diff(Omega0, Omega0y[i]))
            Omega.append(etalon)

        print("final OMEGA")
        print(Omega)

        OmegaUnion = Omega[0]
        for i in range(1,classes):
            OmegaUnion = union(OmegaUnion, Omega[i])

        # step4
        All = np.arange(l)
        while All.size > 0:
            U = []
            for i in range(All.size):
                x = All[i] #it's ID
                y = int(self.y[x]) #it's class
                u = self.NN(Xl[x], Omega[y])
                v = self.NN(Xl[x], diff(OmegaUnion, Omega[y]))
                score = S(Xl[x],Xl[u],Xl[v],self.ro)
                if score > self.theta:
                    U.append(x)

            # step5
            #delete etalons (it's indexes) from X
            for i in range(classes):
                X[i] = diff(X[i], U)
            All = diff(All,U)

            if(len(U)==0): break
            if(All.size == 0): break

            # step6
            for i in range(classes):
                if X[i].size == 0: continue
                etalon = self.FindEtalon(X[i], diff(OmegaUnion, Omega[y]) )
                Omega[i] = union(Omega[i], etalon)

            # recalculate omegas
            OmegaUnion = Omega[0]
            for i in range(1,classes):
                OmegaUnion = union(OmegaUnion, Omega[i])


        return Omega

#method for classification using Fris function
def classify(x, xl, y, etalons, ro=euclidean):
    #how many classes
    cls = int(np.amax(y)+1)
    #array with all achieved best distances
    dist = np.zeros(cls)
    for c in range(cls):
        #all indexes which class equal to C
        idx = y == c
        #take all etalons with class C
        eta = xl[etalons[c],:]
        #take all elementh(without etalons) with class C
        xla = xl[idx,:]
        #take their classes
        ya = y[idx]
        #how many elements with class C
        n = xla.shape[0]
        best = -1e9
        for e in etalons[c]:
            now = 0
            for i in range(n):
                #calculate Fris function "distance"
                now += S(xl[e,:], x, xla[i,:], ro)
            if now > best: best = now
        dist[c] = best
    # print(dist)
    return np.argmax(dist)
    # return dist

#gets x, Xl - viborka, Y - classes, ro - metric
def KNN(x,Xl,Y,k=1, ro=euclidean):
    n = Xl.shape[0]
    dist = np.zeros(n)
    for i in range (n) :
        dist[i] = ro(x,Xl[i,:])
    Xl = Xl[np.argsort (dist), : ]
    Y = Y[np.argsort (dist)]
    cnt = int(np.amax(Y)+1)
    score = [0]*cnt
    for i in range (k):
        curClass = int(Y[i])
        score[curClass] += 1
    return np.argmax(score)
    
def classification_map(classifier, inp, out, xfrom=-7, xto=11, ticks=100):
    # meshgrid
    h = (xto - xfrom) / ticks
    xx, yy = np.arange(xfrom, xto, h), np.arange(xfrom, xto, h)
    xx, yy = np.meshgrid(xx, yy)
    zz = np.empty(xx.shape, dtype=float)
    # classify meshgrid 
    pos = 0
    for x in range(xx.shape[0]):
        for y in range(yy.shape[0]):
            zz[x][y] = classifier(xx[x][y], yy[x][y])
    # display
    print("qwe")
    plt.clf()
    plt.contourf(xx, yy, zz, alpha=0.5) # class separations

Xl,Y = dataFris.DataBuilder().Build("fris")

fris = FRiSSTOLP(Xl,Y,euclidean,0.5,0.0)

res = fris.Main()

U = res[0]
for i in range(1,len(res)):
    U = union(U, res[i])

print(U)

print("etalons")

EtaXl = np.array(Xl[U])
EtaY = np.array(Y[U])

classifierFris = lambda a,b: classify(np.array([a,b]), Xl,Y,res)
classification_map(classifierFris, Xl, Y)
plt.scatter(Xl[:,0], Xl[:,1], c=Y, s=50)
plt.scatter(Xl[U,0], Xl[U,1], c=Y[U], s=500)
plt.show()

classifierKNN = lambda a,b: KNN(np.array([a,b]),Xl,Y)
classification_map(classifierKNN, EtaXl, EtaY)
plt.scatter(Xl[:,0], Xl[:,1], c=Y, s=50)
plt.scatter(Xl[U,0], Xl[U,1], c=Y[U], s=500)
plt.show()