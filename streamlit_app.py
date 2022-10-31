import plotly.express as px
import streamlit as st
import pandas as pd


#import the data available in plotly.express
gapminder_df = px.data.gapminder()

st.set_page_config(
    page_title="DOOCS Viewer", layout="wide"
)

st.title("SASE2 Orbit Viewer")
"""This demo demonstrates SASE2 orbit visualization using DOOCS HIST data for 21.10.2022, local time."""


dfm = pd.read_pickle('doocs_orbit_20221021_viewer.pkl')
minCell = dfm['Cell No'].min()
maxCell = dfm['Cell No'].max()
minValx = dfm['ValueX'].min()
maxValx = dfm['ValueX'].max()
minValy = dfm['ValueY'].min()
maxValy = dfm['ValueY'].max()
dfm['Time'] = dfm.index.strftime("%H:%M:%S.%f").str[:-5]

# Animation year by year basis

animationX = px.line(data_frame=dfm,
          x= 'Cell No',
          y = 'ValueX',
          title = 'X positions',
          labels = {'Cell No': 'Cell', 
                   'ValueX' : 'X.SA2.HIST'},
          hover_name = 'Cell No',
          color_discrete_sequence=px.colors.qualitative.Light24,
          markers=True, 
          range_x = [minCell-0.2, maxCell+0.2],
          range_y = [minValx-0.2, maxValx+0.2],
          animation_frame='Time',
          height=450)
animationX.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
animationX.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
    margin=dict(l=50, r=50, t=40, b=20)
)
animationX.update_yaxes( 
    showline=True, linewidth=2, linecolor='black', showgrid=True
)
animationX.update_xaxes( 
    showline=True, linewidth=1, linecolor='black'
)
st.plotly_chart(animationX, use_container_width=True)

animationY = px.line(data_frame=dfm,
          x= 'Cell No',
          y = 'ValueY',
          title = 'Y positions',
          labels = {'Cell No': 'Cell', 
                   'ValueY' : 'Y.SA2.HIST'},
          hover_name = 'Cell No',
          color_discrete_sequence=px.colors.qualitative.G10,
          markers=True, 
          range_x = [minCell-0.2, maxCell+0.2],
          range_y = [minValy-0.2, maxValy+0.2],
          animation_frame='Time',
          height=450)
animationY.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
animationY.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
    margin=dict(l=50, r=50, t=40, b=20)
)
animationY.update_yaxes( 
    showline=True, linewidth=2, linecolor='black', showgrid=True
)
animationY.update_xaxes( 
    showline=True, linewidth=1, linecolor='black'
)
st.plotly_chart(animationY, use_container_width=True)


st.sidebar.title("Settings")


    # Can be used wherever a "file-like" object is accepted:
    #st.write(dataframe)
# If the user doesn't want to select which features to control, these will be used.


if st.sidebar.checkbox("Show advanced options"):
    # Let the user pick which features to control with sliders.
    #speed = st.sidebar.number_input('Set animation speed', min_value=1, max_value=500, value=50, step=5, format=None, key='speed', help='None', label_visibility="visible")
    control_features = st.sidebar.multiselect(
        "Exclude which cells?",
        ['Cell 1', 'Cell 2', 'Cell 3', 'Cell 4', 'Cell 5', 'Cell 6', 'Cell 7', 'Cell 8', 'Cell 9', 'Cell 10'],
        ['Cell 1'], help='This is still work in progress.'
    )
#else:
    # Don't let the user pick feature values to control.
    #control_features = default_control_features
    #speed = 100

# Insert user-controlled values from sliders into the feature vector.
    
#st.sidebar.slider('Time', 0, 100, 50, 5)



st.sidebar.title("Note")
st.sidebar.write(
    """The app is still in development.
     """
)

st.sidebar.caption("Developed by: Christian Grech (DESY, MXL)")
st.sidebar.caption(f"Streamlit version `{st.__version__}`")