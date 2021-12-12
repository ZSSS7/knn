import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

def circle(a,b,r):
	ɑ = np.arange(0,2 * np.pi,0.01)
	x = a + r * np.cos(ɑ)
	y = b + r * np.sin (ɑ)
	#fig = plt.figure(3)
	#ax = fig.add_subplot(111)
	plt.plot(x,y)
	plt.axis('scaled')
	plt.show()



pointsX = 2+np.random.randn(20,2)
print(pointsX)
plt.figure()
plt.scatter(pointsX[:,0],pointsX[:,1],color = "red")
plt.title("X")
#plt.show()


pointsY = np.random.randn(20,2)
print(pointsY)
plt.figure(2)
plt.scatter(pointsY[:,0],pointsY[:,1])
plt.title("Y")


points = np.append(pointsX,pointsY,axis=0)
print(points.shape)
plt.figure(3)
plt.scatter(points[0:20,0],points[0:20,1],color = "red")
plt.scatter(points[20:40,0],points[20:40,1],color = "blue")
plt.title("XY")

print(points.shape[0])



def kjll(inputx,inputy,k):
    global juli,maxindex
    juli=[]
    for i in range(points.shape[0]):
      x = points[i,0]
      y = points[i,1]
      x1 = inputx
      y1 = inputy
      juli1 = pow((float(x)-x1),2)+pow((float(y)-y1),2)
      juli.append(juli1)

    maxvalue = []
    maxindex = []
    juli2 = juli[:]
    for i in range(k):
        maxvalue1 = min(juli2)
        maxindex1 = juli2.index(maxvalue1)
        juli2[maxindex1] = 10000
        maxvalue.append(maxvalue1)
        maxindex.append(maxindex1)
    labely = sum(i > 20 for i in maxindex)
    labelx = sum(i < 21 for i in maxindex)
    print(juli,maxindex,labelx,labely)
    if labelx>labely:
        print("此点属于x")
    else:
        print("此点属于y")


newx = 3
newy = 0
kjll(newx,newy,3)

plt.scatter(newx,newy,color='yellow')
last=maxindex[-1]
print(last)
print(juli[last])
circle(newx,newy,pow(juli[maxindex[-1]],0.5))