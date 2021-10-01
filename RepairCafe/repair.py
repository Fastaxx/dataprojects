#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:55:46 2021

@author: Louis
"""
#Import streamlit pandas and geopandas
import pandas as pd

data = pd.read_csv('/Users/Louis/GitHub/dataprojects/RepairCafe/repair-cafes.csv', error_bad_lines=False, error_bad_line=False)
print('Shape=>',data.shape)
data.head()