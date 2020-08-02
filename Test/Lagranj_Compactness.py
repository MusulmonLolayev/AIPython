from sklearn.decomposition import PCA, KernelPCA
from sklearn.preprocessing import minmax_scale

from Test.read_data import ToFormArray, ToFormNumpy
from Test.write_file import writeNP
from uz.nuu.datamining.graphic.drawing import mscatter
from uz.nuu.datamining.own.estimations import Lagranj, DecomposionEstimation
from ai.own.fris import Fris
from uz.nuu.datamining.own.functions import Normalizing_Min_Max, Normalizing_Estmation, Normalizing_Estmation1
import numpy as np

def main():

    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\giper_my.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")
    #X, types, y = ToFormNumpy(r"D:\Nuu\Data mining\Articles\PCA operator\Computing\Gastown1.txt")

    print(X)

    return 0

    #y -= 1
    y[y == 2] = 1

    print(np.unique(y, return_counts=True))

    #minmax_scale(X, copy=False)
    Normalizing_Estmation(X, y)

    #return None

    selection_Name = r'\Gasterology12'
    preproccesing_name = r'own'

    img_path = r"D:\Nuu\Data mining\Articles\PCA operator\Computing\Lagranj" + selection_Name + \
               "\images " + preproccesing_name


    save_name = img_path + r"\img"
    save_name += str(X.shape) + ".png";

    path = r"D:\Nuu\Data mining\Articles\PCA operator\Computing\Lagranj" + selection_Name + \
           "/res " + preproccesing_name + ".txt"
    path1 = r"D:\Nuu\Data mining\Articles\PCA operator\Computing\Lagranj" + selection_Name + \
           "/res1 " + preproccesing_name + ".txt"

    p_res = r"D:/Nuu/Data mining/Articles/PCA operator/Computing/Lagranj" + selection_Name + \
           "/data/" + preproccesing_name + "/"
    p_res_PCA = r"D:/Nuu/Data mining/Articles/PCA operator/Computing/Lagranj" + selection_Name + \
            "/data/" + preproccesing_name + "/"

    file = open(path, 'w')
    file1 = open(path1, 'w')

    shape = X.shape

    #Computing for X
    print("Computing for shape " + str(X.shape))
    file.write("Computing for shape " + str(X.shape) + "\n")
    group, comp1, noisy1 = Fris(X, y, types=types, file=file)
    similarity0 = DecomposionEstimation(group, group, X.shape[0])

    print("Similarity between shape  " + str(shape) + " and " + str(X.shape) + " are " + str(similarity0))
    file.write(
        "Similarity between shape  " + str(shape) + " and " + str(X.shape) + " are " + str(similarity0) + "\n")

    writeNP(p_res + str(X.shape) + ".txt", X, y, types=types)

    #PCA
    print("Computing for PCA")
    file.write("Computing for PCA\n")

    #pca = PCA(n_components=2)
    pca = KernelPCA(n_components=2, kernel='poly')
    pca.fit(X, y=y)
    transform = pca.transform(X)
    writeNP(p_res_PCA + str(transform.shape)+ str(X.shape) + ".txt", transform, y, types=[1, 1])
    mscatter(transform, y=y, save_name=save_name)

    group_b, comp2, noisy2 = Fris(transform, y, types, file=file)
    similarity = DecomposionEstimation(group, group_b, X.shape[0])
    print("Similarity between shape  " + str(shape) + " and " + str(transform.shape) + " are " + str(similarity))
    file.write("Similarity between shape  " + str(shape) + " and " + str(transform.shape) + " are " + str(similarity) + "\n")

    file1.write(str(X.shape[1]) + "\t" + str(comp1) + "\t" + str(similarity0) +  "\t" +  str(comp2) + "\t" +  str(similarity) + "\t"  + str(similarity) + "\t"  + str(noisy1) + "\t"  + str(noisy2) +  "\n")

    # 25
    w = Lagranj(X, y, types)

    while X.shape[1] > 2:
        cond = w != w.min()
        X = X[:, cond]
        w = w[cond]

        print("\n" + "*" * 50)
        file.write("\n" + "*" * 50 + "\n")
        print("Computing for shape " + str(X.shape))
        file.write("Computing for shape " + str(X.shape) + "\n")

        # For X
        group_b, comp1, noisy2 = Fris(X, y, types=types, file = file)
        similarity0 = DecomposionEstimation(group, group_b, obj_count=X.shape[0])
        print("Similarity between shape  " + str(shape) + " and " + str(X.shape) + " are " + str(similarity0))
        file.write(
            "Similarity between shape  " + str(shape) + " and " + str(X.shape) + " are " + str(similarity0) + "\n")

        #PCA
        print("Computing for PCA")
        file.write("Computing for PCA\n")

        pca = PCA(n_components=2)
        pca.fit(X, y=y)
        transform = pca.transform(X)

        #Save images
        save_name = img_path + r"\img"
        save_name += str(X.shape) + ".png";
        mscatter(transform, y=y, save_name=save_name)

        group_c, comp2, noisy2 = Fris(transform, y, types, file=file)
        similarity = DecomposionEstimation(group, group_c, X.shape[0])
        similarity1 = DecomposionEstimation(group_b, group_c, X.shape[0])

        print("Similarity between shape  " + str(shape) + " and " + str(transform.shape) + " are " + str(similarity))
        file.write("Similarity between shape  " + str(shape) + " and " + str(transform.shape) + " are " + str(similarity) + "\n")

        file1.write(str(X.shape[1]) + "\t" + str(comp1) + "\t" + str(similarity0) + "\t" + str(comp2) + "\t" + str(
            similarity) + "\t" + str(similarity1) + "\t" + str(noisy1) + "\t" + str(noisy2) + "\n")

        writeNP(p_res + str(X.shape) + ".txt", X, y, types=types)
        writeNP(p_res_PCA + str(transform.shape)+ str(X.shape)+ ".txt", transform, y, types=[1, 1])

    file.close()
    file1.close()

if __name__ == '__main__':
    main()