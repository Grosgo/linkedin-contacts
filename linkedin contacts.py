import pandas as pd
 
pd.set_option('display.max_columns', None)
df = pd.read_excel("Test - Contacts Cleaning(1).xlsx", sheet_name='Database')
df1 = pd.read_excel("Test - Contacts Cleaning(1).xlsx", sheet_name='First List of Job Titles')
df2 = pd.read_excel("Test - Contacts Cleaning(1).xlsx", sheet_name='Second List of Job Titles')
df.fillna('', inplace=True)
df.replace('nan','',regex=True)
print(df['title'].dtypes)

df['Keep Contact'] = 'N'
df.fillna('', regex=True)
df['title'] = df['title'].str.replace('nan','',regex=True)
df['title'] = df['title'].str.replace('NaN','',regex=True)
print(df['title'])
for index, row in df.iterrows():
    for job in df1['Job Title']:
        if (job.lower() in str(row['title']).lower()) or (job.lower() in str(row['last_experience_description']).lower()) or (job.lower() in str(row['last_experience_title']).lower()):
            df.at[index, 'Keep Contact'] = 'Y'
for index, row in df.iterrows():
    for job in df2['Job Title']:
        if (job.lower() in str(row['title']).lower()) or (job.lower() in str(row['last_experience_description']).lower()) or (job.lower() in str(row['last_experience_title']).lower()):
            df.at[index, 'Keep Contact'] = 'Y'
df = df['title','last_experience_title','last_experience_description'].astype(int)
df.fillna('', regex=True)
df.int.replace('nan','',regex=True)
df.replace
 
columns_to_print = ['title', 'last_experience_description', 'last_experience_title', 'Keep Contact']
print(df[columns_to_print].head())
 