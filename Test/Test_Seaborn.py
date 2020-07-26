
import seaborn
import pandas
import pylab as P
import numpy as np
class PlotLocus(object):
      def __init__(self, colorX, colorY, colorpX, colorpY ,excluded_points,lcolorx1,lcolorx2,lcolory1,lcolory2,correspondence_Matrix):
          self.exarr=excluded_points #scatter points excluded by kde
          self.colorx=colorX
          self.colory=colorY
          self.colorpx=colorpX
          self.colorpy=colorpY
          r=np.arange(self.colorx.shape[0])
          self.arr=np.setxor1d(r,self.exarr)
          self.lx1=lcolorx1
          self.lx2=lcolorx2
          self.ly1=lcolory1
          self.ly2=lcolory2
          correspondence_indicies = np.where(M > 0.99)
          self.colorx_corr=self.colorx[correspondence_indicies[0]]
          self.colory_corr=self.colory[correspondence_indicies[0]]
          self.colorpx_corr=self.colorpx[correspondence_indicies[1]]
          self.colorpy_corr=self.colorpy[correspondence_indicies[1]]
      def plot_before_colors(self):
          fig=P.figure(1, figsize=(8,8), dpi=100)
          ax = fig.add_subplot(111)
          X=np.vstack((self.colorx, self.colory)).T
          data = pandas.DataFrame(X, columns=["X", "Y"])
          seaborn.kdeplot(data.X,data.Y,bw='scott',shade=False, cmap="Purples")
          ax.tick_params(axis='both', which='major', direction='in', length=6, width=2)
          ax.scatter(self.colorx[self.exarr], self.colory[self.exarr], s=30, c='g', marker='o', edgecolors='k',facecolors='none')
          ax.scatter(self.colorx, self.colory ,marker='.',s=15,color='b')
          ax.scatter(self.colorpx, self.colorpy, s=15, c='r', marker='d', edgecolor='r')
          for i in range(len(self.colorx_corr)):
              ax.annotate("",
                          xy=(self.colorpx_corr[i], self.colorpy_corr[i]), xycoords='data',
                          xytext=(self.colorx_corr[i], self.colory_corr[i]), textcoords='data',
                          arrowprops=dict(arrowstyle="->",
                          connectionstyle="arc3"),
                          color='0.3'
                          )
          ax.set_xlabel("%s - %s"%(self.lx1,self.lx2), size='medium')
          ax.set_ylabel("%s - %s"%(self.ly1,self.ly2), size='medium')
          ax.set_aspect('auto')

if __name__ == "__main__":
    colorx=np.array([0.4,0.5,-0.3,1.5,0.91,0.66,0.59,-0.11,-0.08,0.12])
    colory=np.array([0.22,-1.15,0.44,0.7,-0.65,-0.21,0.8,-1.1,1.01,0.8])
    colorpx=np.array([0.48,0.45,-0.38,0.5,0.98,0.62,0.77,-0.15,-0.12,0.8])
    colorpx=np.array([0.48,0.45,-0.38,0.5,0.98,0.62,0.77,-0.15,-0.12,0.8,1.8])
    colorpx=np.array([0.48,0.45,-0.38,0.5,0.98,0.62,0.77,-0.15,-0.12,0.8,1.8,2.4])
    colorpy=np.array([0.26,-0.98,-0.1,0.66,-0.7,-0.5,0.84,-0.88,-1.2,0.9,-2.1,1.3])
    lcolorx1='u'
    lcolorx2='i'
    lcolory1='i'
    lcolory2='g'
    M=np.zeros((10,12),float)
    M[1,4]=1
    M[3,5]=1
    M[9,7]=1
    M[0,2]=1
    M[4,10]=1
    p=PlotLocus(colorx,colory,colorpx,colorpy,np.array([2,6,8]),lcolorx1,lcolorx2,lcolory1,lcolory2,M)
    p.plot_before_colors()
    P.show()