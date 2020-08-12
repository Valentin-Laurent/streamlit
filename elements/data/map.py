
import streamlit as st

import numpy as np
import pandas as pd

def run():

    with st.echo():
        @st.cache
        def get_map_data():
            print('get_map_data called')
            return pd.DataFrame(
                    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
                    columns=['lat', 'lon']
                )

        if st.checkbox('Show map', True):
            df = get_map_data()

            st.map(df)
