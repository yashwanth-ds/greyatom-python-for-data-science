# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((new_record,data),axis=0)
print(census.shape)
age=census[:,0]
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.round_(np.mean(age),2)
age_std=np.round_(np.std(age),2)
print(age,min_age,max_age,age_mean,age_std)
race_0=np.where(census[:,2]==0)[0]
print(race_0)
race_1=np.where(census[:,2]==1)[0]
race_2=np.where(census[:,2]==2)[0]
race_3=np.where(census[:,2]==3)[0]
race_4=np.where(census[:,2]==4)[0]
len_0=race_0.shape[0]
len_1=race_1.shape[0]
len_2=race_2.shape[0]
len_3=race_3.shape[0]
len_4=race_4.shape[0]
min1=[len_0,len_1,len_2,len_3,len_4]
minority_race=min1.index(min(min1))
print(minority_race)
senior_citizens=census[np.where(census[:,0]>60)]
senior_citizens_len=senior_citizens[:,0].shape[0]
working_hours_sum=np.sum(census[np.where(census[:,0]>60)][:,6])
print(working_hours_sum)
avg_working_hours=working_hours_sum/senior_citizens_len
print(np.round_(avg_working_hours,2))
high=census[np.where(census[:,1]>10)]
low=census[np.where(census[:,1]<=10)]
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])
print(np.round_(avg_pay_high))
print(np.round_(avg_pay_low))


