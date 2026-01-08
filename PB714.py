import streamlit as st

weight = st.number_input("Enter Weight (kg)")
height = st.number_input("Enter Height (cm)")

if st.button("Calculate BMI"):
    bmi = weight/((height/100)**2)
    st.write(f"Your BMI is : {bmi}")
    if bmi<18:
        st.warning("You are Underweight")
    elif bmi<24:
        st.success("You are normal")
    elif bmi<30:
        st.warning("You are OverWeight")
    else:
        st.error("You are Obese")