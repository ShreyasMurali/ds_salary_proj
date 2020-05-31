# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:43:40 2020

@author: shreyas

"""
import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#  Salary Parsing

df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split("(")[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['min_salary'] = minus_Kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_Kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#  Company Name text only

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#  state field
#  Age of Company
#  Parsing Job Description (pyhton,R etc)