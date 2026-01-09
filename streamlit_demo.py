import streamlit as st
import numpy as np
import datetime as dt
import time
import pandas as pd

st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="",
    layout='wide'
)
st.sidebar.title("Streamlit Topics")
page = st.sidebar.radio("Go to Section",
                        ['UI & Layout',
                         'Input Widgets',
                         'Data Display',
                         'Buttons & Files',
                         'Media & Status'
                         ])

if page == 'UI & Layout':
    st.title("UI Creation & Layout Fundamentals")
    st.header("Text Elements")
    st.subheader("Subheader Example")
    st.text("This is Text")
    st.write("It supports text,number,table,etc.")
    st.markdown("**Markdown** supports _formatting_")

    code ='''
    import numpy as np
    class Matrix:
        def __init__(self,r,c):
            self.rows = r
            self.columns = c
            self.mat = np.zeros((self.rows,self.columns),dtype=int)
        def get_rows(self):
            return self.rows
        def get_cols(self):
            return self.columns
        def set_element(self):
            for i in range(self.rows):
                for j in range(self.columns):
                    self.mat[i][j] = int(input(f"Enter value for {i} row {j} col"))
        def __add__(self,other):
            if self.mat.shape == other.mat.shape:
                return self.mat + other.mat
            else:
                return "Matrices Can't be Added"
        def __mul__(self,other):
            if self.columns == other.rows:
                return np.dot(self.mat,other.mat)
            else:
                return "Matrices can't be Multiplied"
    m1 = Matrix(2,2)
    m2 = Matrix(2,2)
    m1.set_element()
    m2.set_element()
    print(m1+m2)
    print(m1*m2)'''

    st.code(code,language='python')
    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("Success Line")
    with col2:
        st.info("General Information")
    with col3:
        st.warning("Warning")
    with st.expander("Click to Expand"):
        st.write("Hidden Content shown here")

elif page=='Input Widgets':
    st.title("Input Widgets & Interactivity")

    name = st.text_input("Enter Name")
    feedback = st.text_area("Enter Feedback")
    age = st.number_input("Age",1,100,18)
    rating = st.slider('Rate Session',1,10,5)
    course = st.selectbox('Select Course',['FSD-1','Python-1','DE','PS'],index=None)
    days = st.multiselect('Preferred Days',['Mon','Tue','Wed','Thu','Fri'])
    mode = st.radio('Mode',['Online','Offline'])
    subscribe = st.checkbox('Subscribe')
    exam_date = st.date_input('Date',dt.date.today())
    exam_time = st.time_input('Time','now')

    st.markdown("### Live Output")
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Rating: {rating}")
    st.write(f"Course: {course}")
    st.write(f"Preferred Days: {days}")
    st.write(f"Mode: {mode}")
    st.write(f"Subscribed: {subscribe}")
    st.write(f"Date: {exam_date}")
    st.write(f"Time: {exam_time}")

elif page == 'Data Display':
    st.title("Displaying Data")

    data ={
        'Student':['A','B','C'],
        'Marks': [95,85,34],
        'Pass': [True,True,False]
    }

    df = pd.DataFrame(data)

    st.subheader("Table")
    st.table(df)

    st.subheader("Data Frame")
    st.dataframe(df)

    st.subheader("JSON")
    st.json(data)

elif page == 'Buttons & Files':
    st.title('Buttons, File Upload & Download')

    uploaded_file = st.file_uploader('Upload CSV',type=['csv'])

    if uploaded_file:
        df=pd.read_csv(uploaded_file)
        st.dataframe(df)

    if st.button("Generate Sample Data"):
        data = {
        'Student':['A','B','C'],
        'Marks': [95,85,34],
        'Pass': [True,True,False]
        }
        df = pd.DataFrame(data)
        st.table(df)

        csv = df.to_csv(index=False)
        st.download_button(
            'Download CSV',
            csv,
            'marks.csv'
        )
