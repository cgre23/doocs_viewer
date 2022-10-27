import plotly.express as px
import streamlit as st

#import the data available in plotly.express
gapminder_df = px.data.gapminder()

st.set_page_config(
    page_title="DOOCS Viewer3", page_icon="⬇", layout="centered"
)

st.title("DOOCS Viewer")
"""This demo demonstrates SASE2 orbit visualization using DOOCS HIST data"""


st.sidebar.title("Settings")
# If the user doesn't want to select which features to control, these will be used.
default_control_features = ["Young", "Smiling", "Male"]

if st.sidebar.checkbox("Show advanced options"):
    # Let the user pick which features to control with sliders.
    control_features = st.sidebar.multiselect(
        "Exclude which cells?",
        ['Cell 1', 'Cell 2', 'Cell 3', 'Cell 4', 'Cell 5'],
        ['Cell 1'],
    )
else:
    # Don't let the user pick feature values to control.
    control_features = default_control_features

# Insert user-controlled values from sliders into the feature vector.
    
st.sidebar.slider('Time', 0, 100, 50, 5)

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

st.sidebar.title("Note")
st.sidebar.write(
    """The app is still in development.
     """
)

st.sidebar.caption("Developed by: Christian Grech (DESY, MXL)")
st.sidebar.caption(f"Streamlit version `{st.__version__}`")

# Animation year by year basis

animation = px.scatter(data_frame=gapminder_df,
          x= 'gdpPercap',
          y = 'lifeExp',
          size= 'pop',
          color = 'continent',
          title = 'World Life Expectancy and Wealth 1952 - 2007',
          labels = {'gdpPercap': 'Wealth', 
                   'lifeExp' : 'Life expectancy'},
          range_y = [20,95],
          hover_name = 'country',
          animation_frame='year',
          height=650,          
          size_max=100)

st.plotly_chart(animation, use_container_width=True)