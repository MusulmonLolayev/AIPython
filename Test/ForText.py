# Pandas va Numpy kutubxonalarni import qilamiz
import pandas as pd
import numpy as np

df = pd.read_csv('telecom_churn.csv')


df['churn'] = df['churn'].astype('int64')

print(df[df['churn'] == 1].mean())

df.apply(np.max)

d = {'No' : False, 'Yes' : True}
df['international plan'] = df['international plan'].map(d)
df.head()

df = df.replace({'Voice mail plan': d})
df.head()


columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']

df.groupby(['Churn'])[columns_to_show].agg([np.mean, np.std, np.min, np.max])

pd.crosstab(df['Churn'], df['Voice mail plan'], normalize=True)

df.pivot_table(['Total day calls', 'Total eve calls', 'Total night calls'],
['Area code'], aggfunc='mean').head(10)

total_calls = df['Total day calls'] + df['Total eve calls'] + \
                  df['Total night calls'] + df['Total intl calls']
df.insert(loc=len(df.columns), column='Total calls', value=total_calls)

df.head()


df['Total charge'] = df['Total day charge'] + df['Total eve charge'] + df['Total night charge'] + df['Total intl charge']

df.head()



df['Many_service_calls'] = (df['Customer service calls'] > 3).astype('int')

pd.crosstab(df['Many_service_calls'], df['Churn'], margins=True)