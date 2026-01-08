import streamlit as st
import time

st.set_page_config(
    page_title="Vaccination Rate Calculation",
    layout = "centered"
)

st.title("Vaccination Rate Calculation")
st.sidebar.title("Region wise Data")
v = st.sidebar.selectbox("Select country",["US","INDIA","UK","CANADA"])

if v == "US":
    country = "US"
elif v == "INDIA":
    country = "INDIA"
elif v == "UK":
    country = "UK"
elif v == "CANADA":
    country = "CANADA"

population = st.number_input(f'Enter Population of {country}',value=0)
vacc_pop = st.number_input(f'Enter Count of Vaccinated People in {country}',max_value=population)
if st.button("Calculate Vaccination Rate"):
    vacc_rate = vacc_pop/population*100

    progress = st.progress(0)
    for i in range(int(vacc_rate)):
        time.sleep(0.01)
        progress.progress(i+1)

    st.info(f'Vaccination Rate of {country} is {vacc_rate}')

    if vacc_rate>=70:
        st.success(f'Congratulations! , Vaccination Rate of {country} is upto mark')
    else :
        st.warning(f'Vaccination rate of {country} is lesser than required')