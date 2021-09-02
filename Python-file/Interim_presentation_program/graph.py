from matplotlib import pyplot as plt
import numpy as np

x = np.array([300,400,500,600,700,800,900,1000,1500,1600])
y = np.array([2.35,1.98,1.85,5.61,1.55,2.95,1.2,1.95,2,2.75])
"""
xerr=np.array([1.85,1.9,1.85,5.6,0,1.85,0,0,0,0])
yerr=np.array([1.5,0.7,0,0.8,1.5,2.3 ,1.2,1.9,2,3])
"""
fig,ax =plt.subplots()
ax.plot(x,y,label="duration:10 ms")
"""
ax.errorbar(x,y,xerr=xerr,yerr=yerr,capsize=10,fmt='o',ecolor='red',color='black')
"""
ax.legend()

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.ylim([0 ,20])

plt.show()
