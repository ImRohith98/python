#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 16:38:23 2026

@author: rohithreddy
"""

import pandas as pd

data = pd.read_csv("./datasets/data.csv")

"""this will replace space with _ and lowercase"""

data.columns = data.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True).str.replace('.', '_', regex=False)


"""dtypes we can find types of data columns as we can see fee colums 
shows as object but its be flot or int so we will change that """

text_columns=["peak", "all_time_peak", "ref_"]

for col in text_columns:
    data[col] = data[col].replace(' ', 0)
    data[col] = data[col].replace(r'\[.*?\]', 0, regex=True)
    data[col].astype(float)
    

    
print(data.dtypes)


"""this will help to change data type
df['column_name'] = df['column_name'].astype(desired_type)
df = df.astype({'col_1': int, 'col_2': float, 'col_3': str})


"""
"""text_columns=["Peak", "All_Time_Peak", "Ref."]

for col in text_columns:
    data[col] = pd.to_numeric(data[col], errors='coerce').astype('Int64')"""


"""data = data.astype({'Rank': int, 'Peak': int})"""

"""text_columns = data.select_dtypes(include="object").columns

numeric_columns = data.select_dtypes(include="number").columns

for col in text_columns:
    data[col] = data[col].fillna(0)

for col in text_columns:
    data[col] = data[col].str.strip()
    data[col] = data[col].str.lower()
    data[col] = data[col].fillna("unknown")
    """

