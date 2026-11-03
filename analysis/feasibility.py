import sys, pandas as pd, numpy as np
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy import stats
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GroupKFold, StratifiedKFold, cross_val_predict
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score
df = pd.read_csv(sys.argv[1]); out = sys.argv[2]
# dedupe welds that appear in both A and B
u = df.sort_values('set').drop_duplicates('Signal ID', keep='first').copy()
print('unique welds:', len(u)); print(u['Label'].value_counts().to_dict())
F = ['Mean SP [V]','St Dev SP [V]','Mean ST [V]','St Dev ST [V]','Mean SR [V]','St Dev SR [V]']
# good vs defect feature tests
for f in F:
    a=u.loc[u.Label=='SW',f]; 
    for lab in ['LoC','OP']:
        b=u.loc[u.Label==lab,f]; p=stats.mannwhitneyu(a,b).pvalue
        print(f'{f:16s} SW med {a.median():.2f} vs {lab} med {b.median():.2f}  p={p:.1e}')
# ML: naive CV vs grouped CV by process setting (avoid leakage across replicates)
u['grp']=u['set']+'_'+u['Laser Power [W]'].round().astype(int).astype(str)+'_'+u['gap_um'].astype(str)
u['foil']= (u['set']=='C').astype(int)
Xf=u[F+['foil']].values; y=u['Label'].values
rf=RandomForestClassifier(n_estimators=400, random_state=0, class_weight='balanced')
for name,cv,groups in [('stratified 5-fold',StratifiedKFold(5,shuffle=True,random_state=0),None),('grouped by setting 5-fold',GroupKFold(5),u['grp'])]:
    p=cross_val_predict(rf,Xf,y,cv=cv,groups=groups)
    print(f'\n{name}: acc={accuracy_score(y,p):.3f}  recall per class',dict(zip(['LoC','OP','SW'],recall_score(y,p,average=None,labels=['LoC','OP','SW']).round(2))))
    print(pd.DataFrame(confusion_matrix(y,p,labels=['LoC','OP','SW']),index=['LoC','OP','SW'],columns=['pLoC','pOP','pSW']))
    # detection view: defect (LoC/OP) flagged as defect
    d_true=y!='SW'; d_pred=p!='SW'
    print('  defect catch rate (any defect flagged):', round((d_true&d_pred).sum()/d_true.sum(),3), ' false alarm on sound:', round((~d_true&d_pred).sum()/(~d_true).sum(),3))
# process window figure
fig,axes=plt.subplots(1,2,figsize=(11,4.2))
cols={'LoC':'#c0392b','OP':'#e67e22','SW':'#27ae60'}
for ax,(sets,title) in zip(axes,[(['A','B'],'Sets A+B: 300 µm Cu foil'),(['C'],'Set C: 200 µm Ni-plated Cu foil')]):
    s=u[u.set.isin(sets)]
    for lab,g in s.groupby('Label'):
        ax.scatter(g['Laser Power [W]'],g['gap_um'],c=cols[lab],label=lab,alpha=.75,edgecolor='k',lw=.3,s=40)
    ax.set_xlabel('Laser power [W]'); ax.set_ylabel('Part-to-part gap [µm]'); ax.set_title(title); ax.legend()
plt.tight_layout(); plt.savefig(out+'/process_window_preview.png',dpi=130)
u.to_csv(out+'/features_unique.csv',index=False)
