#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:25:56 2021

@author: Louis
"""

import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Cours de l'action
Volume et prix de l'action chez Google""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
 Prix de l'action """ )
st.line_chart(tickerDf.Close)

st.write("""
 Volume  """ )
st.line_chart(tickerDf.Volume)
