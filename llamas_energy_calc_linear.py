"""

conda install -c conda-forge watchdog
pip install streamlit
pip install altair 

Figures and references from https://www.carbonindependent.org/15.html

"""


import streamlit as st 
import scipy as sc
from scipy.stats import beta
import numpy as np
import pandas as pd
import altair as alt

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

x_time_series = range(2020,2050,1) 
step_size = co2_emissions/len(x_time_series)
y = np.linspace(co2_emissions, 0, len(x_time_series))

df = pd.DataFrame()
df['Year'] = x_time_series
df['CO2 emissions (kg)'] = y

basic_chart = alt.Chart(df).mark_line().encode(
    x='Year',
    y='CO2 emissions (kg)'
   ).properties(
    width=700,
    height=400
    )

st.altair_chart(basic_chart)

