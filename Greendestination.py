import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("c:/Users/SOOQ ELASER/OneDrive/Desktop/Green destination project/greendestination (1).csv")
# print(df.head())
# print(df.info())
# print(df['Attrition'].value_counts())

# labels = ['Stayed', 'Left']
# sizes = [1233, 237]
# colors = ['#4CAF50', '#F44336']  
# explode = (0, 0.1)  

# plt.figure(figsize=(6, 6))
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
#         startangle=90, explode=explode, shadow=True)

# plt.title('Employee Attrition Breakdown')
# plt.axis('equal')  

# plt.savefig("attrition_pie_chart.png", dpi=300)
# plt.show()

# sns.set(style="whitegrid")

# df['AgeGroup'] = pd.cut(df['Age'], bins=[18, 25, 30, 35, 40, 45, 50, 60], 
#                         labels=['18–25', '26–30', '31–35', '36–40', '41–45', '46–50', '51+'])


# plt.figure(figsize=(8, 6))
# sns.countplot(data=df, x='AgeGroup', hue='Attrition', palette=['#4CAF50', '#F44336'])

# plt.title('Attrition by Age Group')
# plt.xlabel('Age Group')
# plt.ylabel('Number of Employees')
# plt.legend(title='Attrition')
# plt.tight_layout()

# plt.savefig("attrition_by_age.png", dpi=300)
# plt.show()

# plt.figure(figsize=(8, 6))
# sns.boxplot(data=df, x='Attrition', y='MonthlyIncome', palette=['#4CAF50', '#F44336'])

# plt.title('Monthly Income by Attrition Status')
# plt.xlabel('Attrition')
# plt.ylabel('Monthly Income')
# plt.tight_layout()

# plt.savefig("attrition_by_income.png", dpi=300)
# plt.show()

# income_by_attrition = df.groupby('Attrition')['MonthlyIncome'].mean().reset_index()

# sns.set(style="whitegrid")

# plt.figure(figsize=(6, 5))
# sns.barplot(data=income_by_attrition, x='Attrition', y='MonthlyIncome', palette=['#4CAF50', '#F44336'])

# plt.title('Average Monthly Income by Attrition Status')
# plt.xlabel('Attrition')
# plt.ylabel('Average Monthly Income')
# plt.tight_layout()

# plt.savefig("avg_income_by_attrition.png", dpi=300)
# plt.show()

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='YearsAtCompany', hue='Attrition', multiple='stack', 
             palette=['#4CAF50', '#F44336'], binwidth=1)

plt.title('Attrition by Years at Company')
plt.xlabel('Years at Company')
plt.ylabel('Number of Employees')
plt.xticks(range(0, df['YearsAtCompany'].max() + 1))
plt.tight_layout()

plt.savefig("attrition_by_tenure.png", dpi=300)
plt.show()