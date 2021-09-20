#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:43:21 2021

@author: Louis
"""
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

######################
# Header
######################

image = Image.open('/Users/Louis/GitHub/dataprojects/ADNcount/dna.png')

st.image(image, width=300)

st.write("""
# Décompte des nucléotides d'une séquence ADN

***
""")


######################
# Entrée de la séquence
######################

st.sidebar.header('Entrer la séquence ADN')
st.header('Entrer la séquence ADN')

sequence_input = ">Séquence ADN 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Séquence", sequence_input, height=250)
sequence = st.text_area("Séquence", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] 
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('Entrée')
sequence

st.header('Comptage Nucléotides')

### 1. Print dictionary
st.subheader('1. Dictionnaire')
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

X

### 2. Texte
st.subheader('2. Texte')
st.write('Il y a  ' + str(X['A']) + ' adenine (A)')
st.write('Il y a  ' + str(X['T']) + ' thymine (T)')
st.write('Il y a ' + str(X['G']) + ' guanine (G)')
st.write('Il y a  ' + str(X['C']) + ' cytosine (C)')

### 3. Tableau
st.subheader('3. Tableau')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'Nombre'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Graphe
st.subheader('4. Graphe')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='Nombre'
)
p = p.properties(
    width=alt.Step(80)  
)
st.write(p)