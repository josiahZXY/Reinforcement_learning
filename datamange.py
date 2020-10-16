import pandas as pd
import numpy as np
x=[]
y=[]
position=[]
del_index=[]
df = pd.read_csv('sarsa.csv')
for i in range(df.shape[0]):
    if df.iat[i, 0] == 'terminal':
        x.append(0)
        y.append(0)
        position.append(0)
        continue
    else:
        a = df.iat[i, 0]
        a = a.replace('.', '').replace('0', '').replace('[', '').replace(']', '').replace(' ', '')
        l = list(map(int, a.split(',')))
        x.append(l[0] + 15)
        y.append(l[1] + 15)
        b = [df['0'][i], df['1'][i], df['2'][i], df['3'][i]]
        position.append(b.index(max(b)))

        #df['best'] = position
df['x'] = x
df['y'] = y
df['best']=position
df=df.sort_values('y')
for j in range(df.shape[0]):
    if df.iat[j,0]=='terminal':
        del_index.append(j)
df=df.drop(index=del_index)
df.to_csv('sarsa.csv', index=False)

