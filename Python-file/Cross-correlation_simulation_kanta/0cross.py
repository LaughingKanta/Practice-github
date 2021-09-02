import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation 

##遅延がある信号の作成
target_sig=np.random.normal(size=10000)*1.0
delay=25000
##一つ目の信号作成
sig1=np.random.normal(size=32768)*0.01
sig1[delay:delay+10000]+=target_sig
##二つ目の信号作成
sig2=np.random.normal(size=32768)*0.01
sig2[:10000]+=target_sig
##遅延時間を求める
corr=np.correlate(sig1,sig2,"full")
estimated_delay=corr.argmax()-(len(sig2)-1)
##描画
plt.subplot(4,1,1)
plt.ylabel("sig1")
plt.plot(sig1)

plt.subplot(4,1,2)
plt.ylabel("sig2")
plt.plot(sig2,color="g")

plt.subplot(4,1,3)
plt.ylabel("fit")
plt.plot(np.arange(len(sig1)),sig1)
plt.plot(np.arange(len(sig2))+estimated_delay,sig2)
plt.xlim([0,len(sig1)])

plt.subplot(4,1,4)
plt.ylabel("corr")
plt.plot(np.arange(len(corr))-len(sig2)+1,corr,color="r")
plt.xlim([0,len(sig1)])

plt.show()

