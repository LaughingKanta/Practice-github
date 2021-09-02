import matplotlib.pyplot as plt
import numpy as np

def plot_polar(labels,values,imgname):
    angles=np.linspace(0,2*np.pi,len(labels)+1,endpoint=True)
    values=np.concatenate((values,[values[0]]))
    fig=plt.figure()
    ax=fig.add_subplot(111,polar=True)
    ax.plot(angles, values, 'o-')  # 外枠
    ax.fill(angles, values, alpha=0.25)  # 塗りつぶし
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)  # 軸ラベル
    ax.set_rlim(0 ,250)
    fig.savefig(imgname)
    ax.set_thetalim([-90 ,90])
    plt.close(fig)

labels =['-90','-75','-60','-45','-30','-15','0','15','30','45','60','75','90']
values=[53.51760035
,53.81760035
,56.71760035
,57.21760035
,67.21760035
,72.81760035
,76.91760035
,76.31760035
,70.81760035
,64.51760035
,56.11760035
,55.61760035
,52.51760035
]
plot_polar(labels,values,"a.png")