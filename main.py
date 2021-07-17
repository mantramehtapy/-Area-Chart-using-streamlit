#use this command to install pakages

# pip3 install streamlit

#pip3 install pandas

#pip3 install numpy

import streamlit as st
import pandas as pd
import numpy as np

latest_iterations = st.empty()
chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])
st.area_chart(chart_data)
expander = st.beta_expander("FAQ")
expander.text("created by Mantra.Mehta")
st.write("check out my [discord](https://discord.com/invite/NCyRpbqQJT)")
st.write("check out my [github](https://github.com/mantramehtapy)")
st.write("check out my [youtube channel](https://www.youtube.com/channel/UC0TMsiwESD3AjacKiBDc0eQ)")
