import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


arr_2d=np.array([20,20,	20,	20	,9.310746479	,1.95,	2.089258242,	4.39089968	,20	,4.401136217	,20
,20,	3.231098884,	20	,7.669419796,	7.981227976	,1.2	,1.41509717	,1.25	,4.916299421	,3.259601203	,20
,20	,13.86001443	,3.217530109	,20	,2.549509757	,2.951694429,	2.419194081	,4.164732885	,3.217530109	,2.571478174	,20
,6.39413794	,3.376758801	,2.732215218	,1.589024858	,4.501388675	,1.55	,7.468768305	,4.049691346	,3.423448554	,1.930025907	,3.400367627
,0.801560977,	2.888771365	,2.387990787	,0.87321246	,5.380752735	,5.607361233	,3.056550343	,3.045077996	,2.680018657	,4.644620544	,20
,14.93393786	,3.551056181	,2.250555487	,1.931967909	,1.101135777	,1.850675552	,3.508917212	,1.931967909	,1.941648784	,20	,20
,4.802343178	,1.626345597	,5.991034969	,20	,1.303840481	,1.978004044	,1.591383046	,3.020347662	,6.711929678	,4.455333882	,20
,20	,1.610124219	,2.285278976	,0.531507291	,6.312685641	,2.350531855	,2.976995129	,13.86767825	,3.181980515	,6.711929678	,20]).reshape((8,11))
df = pd.DataFrame(data=arr_2d, index=['100', '90', '80', '70','60','50','40','30'], columns=['-50', '-40', '-30', '-20','-10','0','10','20','30','40','50'])
print(df)
plt.figure()
ax=sns.heatmap(df,vmax=20,vmin=0,center=4,cmap='Blues')
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.show()
