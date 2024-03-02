import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import os
from PIL import Image
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Singapore Flat Resale modelling by KAVIPRIYA!!!", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart:   Singapore Resale Flat Prices Predicting")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# with st.headbar:
SELECT = option_menu(
    menu_title=None,
    options=["Home", "Explore Data", "Contact"],
    icons=["house", "bar-chart", "at"],
    default_index=2,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "white", "size": "cover", "width": "100"},
            "icon": {"color": "black", "font-size": "20px"},

            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
            "nav-link-selected": {"background-color": "#6F36AD"}})

#----------------Home----------------------#

if SELECT == "Home":

 st.header('Singapore Resale Flat Prices Predicting')
 st.subheader("Based on the properties of HDB flats in Singapore,the resale price can be predicted by data mining methods. This report will show how we did implement the knowledge we learnt, practice EDA, data preprocessing and model training and complete the prediction of the resale price of HDB flats in Singapore")
 st.subheader('Skills take away From This Project:')
 st.subheader('Data Wrangling, EDA, Model Building, Model Deployment')
 st.subheader('Domain:')
 st.subheader('Real Estate')

if SELECT == "Explore Data":
 fl = st.file_uploader(":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "xls"]))
 if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding="ISO-8859-1")
 else:
    os.chdir(r"C:\\Users\\KAVIPRIYA\\Desktop")
    df = pd.read_csv("C:\\Users\\KAVIPRIYA\Desktop\\ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv")
 st.sidebar.header("Choose your filter: ")

 # Create for town
 town = st.sidebar.multiselect("Pick your town", df["town"].unique())
 if not town:
     df2 = df.copy()
 else:
     df2 = df[df["town"].isin(town)]

 # Create for street_name
 street_name = st.sidebar.multiselect("Pick the street_name", df2["street_name"].unique())
 if not street_name:
     df3 = df2.copy()
 else:
     df3 = df2[df2["street_name"].isin(street_name)]

 # Filter the data based on town, street_name

 if not town and not street_name:
     filtered_df = df
 elif not street_name:
     filtered_df = df[df["town"].isin(town)]
 elif not town:
     filtered_df = df[df["street_name"].isin("street_name")]
 elif street_name:
     filtered_df = df3[df["street_name"].isin("street_name")]
 elif town:
     filtered_df = df3[df["town"].isin(town)]
 elif town and street_name:
     filtered_df = df3[df["town"].isin(town) & df3["street_name"].isin(street_name)]
 else:
     filtered_df = df3[df3["town"].isin(town) & df3["street_name"].isin(street_name)]

 flat_type_df = filtered_df.groupby(by=["flat_type"], as_index=False)["resale_price"].sum()

 col1, col2 = st.columns(2)
 with col1:
    st.subheader("flat_type_ViewData")
    fig = px.bar(flat_type_df, x="flat_type", y="resale_price", text=['${:,.2f}'.format(x) for x in flat_type_df["resale_price"]],
                 template="seaborn")
    st.plotly_chart(fig, use_container_width=True, height=200)

 with col2:
    st.subheader("town_ViewData")
    fig = px.pie(filtered_df, values="resale_price", names="town", hole=0.5)
    fig.update_traces(text=filtered_df["town"], textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

 cl1, cl2 = st.columns((2))
 with cl1:
    with st.expander("flat_type wise resale_price"):
        st.write(flat_type_df.style.background_gradient(cmap="Blues"))
        csv = flat_type_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="flat_type.csv", mime="text/csv",
                           help='Click here to download the data as a CSV file')

 with cl2:
    with st.expander("town wise resale_price"):
        town = filtered_df.groupby(by="town", as_index=False)["resale_price"].sum()
        st.write(town.style.background_gradient(cmap="Oranges"))
        csv = town.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="town.csv", mime="text/csv",
                           help='Click here to download the data as a CSV file')

 # Create a scatter plot
 data1 = px.scatter(filtered_df, x="town", y="street_name", color="flat_type")
 data1['layout'].update(title="flat_type in the street_name and town wise data using Scatter Plot.",
                        titlefont=dict(size=20), xaxis=dict(title="town", titlefont=dict(size=20)),
                        yaxis=dict(title="street_name", titlefont=dict(size=20)))
 st.plotly_chart(data1, use_container_width=True)

 with st.expander("Detailed Room Availability and resale_price View Data in the street_name"):
     st.write(filtered_df.iloc[:500, 1:20:2].style.background_gradient(cmap="Oranges"))

 # Download orginal DataSet
 csv = df.to_csv(index=False).encode('utf-8')
 st.download_button('Download Data', data=csv, file_name="Data.csv", mime="text/csv")

 import plotly.figure_factory as ff

 st.subheader(":point_right: town wise flat_type and Resale_price")
 with st.expander("Summary_Table"):
    df_sample = df[0:5][["town", "street_name", "storey_range", "flat_type", "resale_price", "floor_area_sqm", "flat_model"]]
    fig = ff.create_table(df_sample, colorscale="Cividis")
    st.plotly_chart(fig, use_container_width=True)

# ----------------------Contact---------------#

if SELECT == "Contact":
    Name = (f'{"Name :"}  {"KAVIPRIYA"}')
    mail = (f'{"Mail :"}  {"kavipriyadevaraj1999@gmail.com"}')
    description = "An Aspiring DATA-SCIENTIST..!"
    social_media = {
        "GITHUB": "https://github.com/Kavipriya2/Guvi_Capstone_Projects"}

    st.header('Singapore Resale Flat resale_prices Predicting')
    st.subheader(
            "The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts the resale prices of flats in Singapore. This predictive model will be based on historical data of resale flat transactions, and it aims to assist both potential buyers and sellers in estimating the resale value of a flat.")
    st.write("---")
    st.subheader(Name)
    st.subheader(mail)

    st.write("#")
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")
