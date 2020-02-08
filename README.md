# dcarb-consumption-dashboard

Simple dashboard designed with [streamlit](https://www.streamlit.io/). Built as part of the Valtech Climate Emergency Hackathon. 

Plots energy consumption in KWh to emissions in kg CO2. The second chart gives shows a sliding scale towards full decarbonisation from energy consumption.  

You will need the Anaconda python environment installed -- [here](https://www.anaconda.com/distribution/#download-section)

If you want to bork your Spyder environment do this: 
`conda install -c conda-forge watchdog`

    conda install -c conda-forge watchdog
    pip install -r requirements.txt

Otherwise setup a new conda environment. For example:

    conda create --name env_streamlit python=3.7
    conda activate env_streamlit
    conda config --set pip_interop_enabled True

    conda install -c conda-forge watchdog
    pip install -r requirements.txt

## Install instructions 
To run `streamlit run llamas_energy_calc_exponential.py`

## References

Conversation details from [https://www.carbonindependent.org/15.html](https://www.carbonindependent.org/15.html)

## Screenshot 

<img src="./consumption_dashboard.png " height="600" align="middle">
