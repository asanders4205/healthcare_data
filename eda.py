import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('healthcare_dataset.csv')

print(df.head())
print(df.columns)

print(df['Medical Condition'].unique())
#Output: ['Cancer' 'Obesity' 'Diabetes' 'Asthma' 'Hypertension' 'Arthritis']

# Ideas: group condition by age

df.loc[df['Age'].between(0,18), 'Age Group'] = '0-18'
df.loc[df['Age'].between(19,30), 'Age Group'] = '19-30'
df.loc[df['Age'].between(31,40), 'Age Group'] = '31-40'
df.loc[df['Age'].between(41,50), 'Age Group'] = '41-50'
df.loc[df['Age'] > 50, 'Age Group'] = '50+'
print(df.head())

# Print count of each condition by age group
illness_by_age = df.groupby(['Age Group', 'Medical Condition']).size().reset_index(name='Count')
print(illness_by_age)

#Heatmap of illness by age group
pivot_table = illness_by_age.pivot(index='Age Group', columns='Medical Condition', values='Count').fillna(0)

plt.figure(figsize=(10,6))
sns.heatmap(pivot_table, annot=True, fmt='g', cmap='YlGnBu')

plt.title('Medical Condition by Age Group')
plt.xlabel('Medical Condition')
plt.ylabel('Age group')
plt.tight_layout()
plt.show()
