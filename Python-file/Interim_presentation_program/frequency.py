from matplotlib import pyplot as plt
import numpy as np
plt.rcParams["font.family"] = "Arial"
x = np.array([20,30,40,50,60,70,80,90,100])
y = np.array([63.8176,74.2176,81.2176,82.0176,76.3176,72.2176,70.8176,62.4176,57.5176])

plt.plot(x,y,marker='o',color='turquoise')
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
print(np.std(y, ddof=1))

plt.ylim([0,100])

plt.show()