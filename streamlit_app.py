import plotly.express as px
import streamlit as st

#import the data available in plotly.express
gapminder_df = px.data.gapminder()

st.set_page_config(
    page_title="DOOCS Viewer3", page_icon="⬇", layout="centered"
)

st.title("DOOCS Viewer")
"""This demo demonstrates  using [Nvidia's Progressive Growing of GANs](https://research.nvidia.com/publication/2017-10_Progressive-Growing-of) and 
Shaobo Guan's [Transparent Latent-space GAN method](https://blog.insightdatascience.com/generating-custom-photo-realistic-faces-using-ai-d170b1b59255) 
for tuning the output face's characteristics. For more information, check out the tutorial on [Towards Data Science](https://towardsdatascience.com/building-machine-learning-apps-with-streamlit-667cef3ff509)."""


st.sidebar.title("Features")
# If the user doesn't want to select which features to control, these will be used.
default_control_features = ["Young", "Smiling", "Male"]

if st.sidebar.checkbox("Show advanced options"):
    # Let the user pick which features to control with sliders.
    control_features = st.sidebar.multiselect(
        "Control which features?",
        ['Cell 1', 'Cell 2'],
        ['Cell 3'],
    )
else:
    # Don't let the user pick feature values to control.
    control_features = default_control_features

# Insert user-controlled values from sliders into the feature vector.
    
st.sidebar.slider('Time', 0, 100, 50, 5)

st.sidebar.title("Note")
st.sidebar.write(
    """The app is still in development.
     """
)

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
          log_x = True,
          range_y = [20,95],
          hover_name = 'country',
          animation_frame='year',
          height=650,          
          size_max=100)

st.plotly_chart(animation, use_container_width=True)