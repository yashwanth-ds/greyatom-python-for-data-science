# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank= pd.read_csv(path)
print(bank.info())
categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var.shape)
numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var.shape)
#Code starts here

banks=bank.drop('Loan_ID',axis=1)
print(banks.shape)
print(banks.isnull().sum())
#bank_mode=banks.mode()

for col in banks.columns:
    banks[col].fillna(banks[col].mode()[0],inplace=True)
#banks=banks.fillna(banks.mode)
#print(banks.isnull().sum().values.sum())
#print(banks['LoanAmount'])
banks=banks.astype({'LoanAmount':'float64'})
avg_loan_amount=banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc='mean')

avg_loan_amount['LoanAmount'][1]

banks1=banks[banks['Self_Employed']=='Yes']
loan_approved_se=len(banks1[ banks1['Loan_Status']=='Y'])
banks2=banks[banks['Self_Employed']=='No']
loan_approved_nse=len(banks2[ banks2['Loan_Status']=='Y'])
percentage_se=(loan_approved_se/614)*100
percentage_nse=(loan_approved_nse/614)*100
print(percentage_nse,percentage_se)
banks['Loan_Amount_Term']=banks['Loan_Amount_Term'].apply(lambda x:x/12)
print(banks.head())
loan_term=banks['Loan_Amount_Term']
big_loan_term=banks[banks['Loan_Amount_Term']>=25]
print(len(big_loan_term))
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.mean()
print(mean_values.iloc[1,0])



