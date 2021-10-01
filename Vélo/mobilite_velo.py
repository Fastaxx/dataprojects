#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:58:51 2021

@author: Louis
"""

import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

st.title('Carte Mobilité à Vélo')
map_1 = KeplerGl(height=400)
keplergl_static(map_1)