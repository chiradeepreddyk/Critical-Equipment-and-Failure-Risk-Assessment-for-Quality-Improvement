import sys, os, glob, re
import pandas as pd, numpy as np
X = sys.argv[1]; SIG = sys.argv[2]
frames=[]
for s in ['A','B','C']:
    d = pd.read_excel(X, sheet_name=s).dropna(how='all')
    d = d.rename(columns={'Laser power [W]':'Laser Power [W]','Effective gap [µm]':'gap_um','Part-to-part gap [µm]':'gap_um'})
    d['set']=s; frames.append(d)
df = pd.concat(frames, ignore_index=True)
print('rows per set:', df.groupby('set').size().to_dict(), 'total', len(df))
print('missing per col:\n', df.isna().sum()[df.isna().sum()>0])
print('dup signal ids:', df['Signal ID'].duplicated().sum())
print('\nlabel counts:\n', pd.crosstab(df['set'], df['Label'], margins=True))
# match with CSV files and header Result
hdr=[]
for s in ['A','B','C']:
    for f in glob.glob(os.path.join(SIG, f'Dataset_{s}', '*.csv')):
        meta={}
        with open(f, encoding='latin-1') as fh:
            for _ in range(10):
                line=fh.readline().strip()
                if ':' in line: k,v=line.split(':',1); meta[k.strip()]=v.strip()
        hdr.append({'set':s,'Signal ID':int(os.path.basename(f)[:-4]),'Result':meta.get('Result'),'Config':meta.get('Configuration'),'Date':meta.get('Date'),'Duration':meta.get('Duration')})
h=pd.DataFrame(hdr)
m=df.merge(h,on=['set','Signal ID'],how='outer',indicator=True)
print('\nmatch xlsx<->csv:', m['_merge'].value_counts().to_dict())
print('\nLabel vs CSV header Result:\n', pd.crosstab(m['Label'], m['Result']))
print('\nDurations:', h['Duration'].value_counts().to_dict())
print('\nDates range:', pd.to_datetime(h['Date']).min(), '->', pd.to_datetime(h['Date']).max())
print('\nPower/gap levels per set:')
for s,g in df.groupby('set'):
    print(s, 'power', sorted(g['Laser Power [W]'].unique()), 'gap', sorted(g['gap_um'].unique()))
c=df[df.set=='C']
print('\nSet C DP/TS by label:\n', c.groupby('Label')[['Weld pen., DP [µm]','Thick. at throat, TS [µm]']].describe().round(1).T)
# label rule check for C (TL=300 steel? upper=200)
print('\nreplicates per (set,power,gap):\n', df.groupby(['set','Laser Power [W]','gap_um']).size().value_counts().to_dict())
mixed = df.groupby(['set','Laser Power [W]','gap_um'])['Label'].nunique()
print('settings with mixed labels:', (mixed>1).sum(), 'of', len(mixed))
df.to_csv(sys.argv[3], index=False)
