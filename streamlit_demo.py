import streamlit as st
import numpy as np
import datetime as dt
import time
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config( page_title="StreamLit Demo",
    page_icon="",
    layout='wide')

st.sidebar.title("StreamLit Topics")
page = st.sidebar.radio("Go to section",
                        ['UI and Layout',
                         'Input Widgets',
                         'Data Display',
                         'Buttons and File',
                         'Media and Status',
                         "Charts and Visualiztion"])

if page=='UI and Layout':

    
    st.title("UI creation & Layout Fundamentals")
    st.header("Text ELements")
    st.subheader("SubHeader Example")
    st.text("This is Text")
    st.write("It supports text,number,table,etc.")
    st.markdown("**Markdown** supports_formatting")

    code='''
    import numpy as np

    class Matrix:
        def __init__(self,rows,cols):
            self.rows=rows
            self.cols=cols
            self.mat=np.zeros((self.rows,self.cols),dtype=int)
        
        def get_rows(self):
            return self.rows
        
        def get_cols(self):
            return self.cols
        
        def setElements(self):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.mat[i][j]=int(input(f"Enter value for {i} row {j} column :---> "))
        
        def __add__(self,other):
            if self.mat.shape==other.mat.shape:
                return self.mat+other.mat
            else:
                return "Matrices can't be Added"
        
        def __mul__(self,other):
            if self.cols==other.rows:
                return np.dot(self.mat,other.mat)
            else:
                return "Matrices can't be multiplied"
            
    m1=Matrix(2,2)
    m2=Matrix(2,2)
    m1.setElements()
    m2.setElements()
    print(m1+m2)
    print(m1*m2)'''

    st.code(code,language='python')
    st.divider()


    col1,col2,col3=st.columns(3)
    with col1:
        st.success("Success Line")
    with col2:
        st.info("General Information")
    with col3:
        st.warning("Warning")

    with st.expander("Click to expand"):
        st.write("Hidden Content shown here")


elif page=='Input Widgets':
    st.title("Input Widgets and Interactivity")
    name = st.text_input("Enter Name")
    feedback = st.text_area("Enter Feedback")
    age = st.number_input("Age",1,100,18)
    rating = st.slider("Rate Session",1,10,5)
    course = st.selectbox("Select course",['FSD','Python-1','DE','PS'],index=None)
    days = st.multiselect("Preferred Days",['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
    mode = st.radio("Mode",["Online","Offline"])
    subscribe = st.checkbox("Subscribe")
    exam_date = st.date_input("Date",dt.date(2026,1,2))
    exam_time = st.time_input("Time",dt.time(11,55))

    st.markdown("### Live Output")
    st.write(f"Name : {name}")
    st.write(f"Age : {age}")
    st.write(f"Rating : {rating}")
    st.write(f"Course : {course}")
    st.write(f"Preferred days : {days}")
    st.write(f"Mode : {mode}")
    st.write(f"Subscribed : {subscribe}")
    st.write(f"Date : {exam_date}")
    st.write(f"Time : {exam_time}")

elif page=='Data Display':
    st.title("Displaying Data")

    data = {
        'Student':['A','B','C'],
        'Marks':[95,85,34],
        'Pass':[True,True,False]
    }

    df =pd.DataFrame(data)

    st.subheader("Table")
    st.table(df)

    st.subheader("Data Frame")
    st.dataframe(df)

    st.subheader("JSON")
    st.json(data)

elif page=='Buttons and File':
    st.title("Buttons, File Upload and Download")
    uploaded_file = st.file_uploader("Upload CSV",type=['csv'])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

    if st.button("Generate Sample Data"):
        data = {
        'Student':['A','B','C'],
        'Marks':[95,85,34],
        'Pass':[True,True,False]
    }
        df = pd.DataFrame(data)
        st.table(df)


        csv = df.to_csv(index=False)
        st.download_button(
            'Download CSV',
            csv,
            'marks.csv'
        )

elif page=='Media and Status':
    st.title("Media and Status")

    st.success("Success Code")
    st.info("Info Status")
    st.warning("Warning Status")
    st.error("Error Status")

    # Progress Bar (Spinner)

    if st.button("Start Task"):
        progress = st.progress(0)
        with st.spinner("Processing...."):
            for i in range(100):
                time.sleep(0.1)
                progress.progress(i+1)
        st.success("Task Completed...")

    st.divider()
    st.subheader("MEdia Display")
    st.image('python.jfif',caption='Python',width='stretch')
    st.audio("sampleaudio.mp3")
    st.video("samplevideo.mp4")
    st.image("https://picsum.photos/600/300")

elif page == "Charts and Visualiztion":
    st.title("Charts and Visualiztion")

    x = np.arange(1,101)
    y = np.random.randint(1,100,100)
    st.subheader("Matplotlib Line Chart")
    plt.figure()
    plt.plot(x,y,marker="*")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Line Chart")
    st.pyplot(plt)

    st.divider()
    st.divider()

    st.subheader("Matplotlib Histogram")

    plt.figure()
    plt.hist(y,color="red")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Histogram")
    st.pyplot(plt)

    st.divider()
    st.divider()

    st.subheader("Stream-Lit In-built Charts")

    data = {
        'X' : x,
        'Y' : y
    }
    df = pd.DataFrame(data)
    st.subheader("Line Chart")
    st.line_chart(df['Y'],color="#7bff0087")
    st.divider()
    st.subheader("Bar Graph")
    st.bar_chart(df['Y'],color="#e100ff85")
    st.divider()
    st.subheader("Area Chart")
    st.area_chart(df['Y'])
    st.divider()