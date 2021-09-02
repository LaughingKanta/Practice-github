import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation

fig=plt.figure()
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)

##各コマの画像を格納
image_list=[]
##delayの初期


##信号の作成
##遅延がある信号の作成
target_sig=np.random.normal(size=10000)*1.0
##一つ目の信号作成
sig1=np.random.normal(size=32768)*0.0
##二つ目の信号作成
sig2=np.random.normal(size=32768)*0.0
sig2[:10000]+=target_sig
delay=0

for i in range(50):
     sig1[delay:delay+10000]+=target_sig 
     image1=ax1.plot(sig1)
     image2=ax2.plot(sig2)
     corr=np.correlate(sig1,sig2,"full")
     image3=ax3.plot(corr)
     image_list.append(image1+image2+image3)
     sig1[delay:delay+10000]-=target_sig
     delay+=300

ani=ArtistAnimation(fig,image_list,interval=200)
ani.save("test.gif")


