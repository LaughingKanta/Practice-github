import math
from matplotlib import scale 
import numpy as np
from scipy.fftpack import fft2
import matplotlib.pyplot as plt

from matplotlib.animation import ArtistAnimation

fig=plt.figure()
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)

##各コマの画像を格納
image_list=[]
"initialize"
fStart=80000
fEnd=40000
BatCallConstant=0.001
"make fm sound"
pi =np.pi
Boxnum=32768
fr=192000
sig1=[0]*Boxnum
sig2=[0]*Boxnum
nframes=int(0.01*fr+1)
arg= (BatCallConstant*fEnd)/fStart
call=[]
t1=[]
fStart=fStart/100
fEnd=fEnd/100
for i in range(nframes):
 t = float(i)/fr*100
 t1.append(i/1000)
 call.append(np.sin(2.*pi*((fStart/(fStart-BatCallConstant*fEnd))*((fStart-fEnd)*np.float_power(arg, t)/math.log(arg)+(1-BatCallConstant)*fEnd*t))))

delay=0
sig2[:10000]+=call


for i in range(50):
     sig1[delay:delay+10000]+=call 
     image1=ax1.plot(sig1)
     
     image2=ax2.plot(sig2)
     corr=np.correlate(sig1,sig2,"full")
     image3=ax3.plot(np.arange(len(corr))-len(sig2)+1,corr)
     image_list.append(image1+image2+image3)
     sig1=[0]*Boxnum
     delay+=450

ani=ArtistAnimation(fig,image_list,interval=10)
plt.show()

"""
for i in range(50):
     sig1[delay:delay+10000]+=call 
     image1=ax1.plot(sig1)
     
     image2=ax2.plot(sig2)
     corr=np.correlate(sig1,sig2,"full")
     image3=ax3.plot(np.arange(len(corr))-len(sig2)+1,corr)
     image_list.append(image1+image2+image3)
     sig1=[0]*Boxnum
     delay+=450

ani=ArtistAnimation(fig,image_list,interval=10)
plt.show()
"""

"""
fft_data=np.abs(np.fft.fft(call))
fft_freq=np.fft.fftfreq(10000,1/192000)
plt.plot(fft_freq[1:int(10000/2)],fft_data[1:int(10000/2)])
plt.show()
"""

