"""

conda install -c conda-forge watchdog
pip install streamlit
pip install altair 

Figures and references from https://www.carbonindependent.org/15.html

"""


import streamlit as st 
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
import altair as alt


def func(x, adj1,adj2):
    return ((x+adj1) ** pw) * adj2

st.write("""
         # Your Energy Journey to Net Zero
         """)

st.header('Information of your consumption')

x = st.slider("What is your energy consumption? (KWh)", 0, 10000, 5000)

y = st.slider("What percentage is your renewable energy? (%)", 0, 100, 50)
st.write("Your renewable percentage is:", y)

z = 100-y #  Amount of energy used

st.write("Your non-renewable percentage is:", z)

#The average electricity consumption is 4,800 kWh per household

#The CO2 emission factor used is 0.309 kge / kWh [BEIS (2018), 44]
#This includes an allowance for the 7.8% of transmission/distribution losses on the national grid [44].
co2_emissions = 0.309 * x * z # conversion factor * non-renewable energy

st.write("Carbon emissions are 0.309 x non-renewable emissions")
st.write("Your estimated carbon emissions are:", co2_emissions, " kg")

st.header('Information of your journey to zero emissions')

x = [2020, 2050]
y = [co2_emissions, 0.01]

pw = st.slider("How quickly will you decarbonise?", 0, 10, 2)

A = np.exp(np.log(y[0]/y[1])/pw)
a = (x[0] - x[1]*A)/(A-1)
b = y[0]/(x[0]+a)**pw

xf = np.linspace(2020,2050,31)

df = pd.DataFrame()
df['Year'] = xf
df['CO2 emissions (kg)'] = func(xf, a, b)

basic_chart = alt.Chart(df).mark_line().encode(
    x='Year',
    y='CO2 emissions (kg)'
   ).properties(
    width=700,
    height=400
    )

st.altair_chart(basic_chart)

