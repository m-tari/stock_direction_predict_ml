import streamlit as st
import pandas as pd
import re

st.write(
'''
# Will stock X's price go up or down the next day?

'''
)

data = pd.read_csv('./datasets/ohlc_data.csv')
pred_df = pd.read_csv('./predictions/predictions.csv')

movement_to_show = st.selectbox('Select the movement prediction', ['Upward','Downward'])

if movement_to_show == 'Upward':

	pred_df_show = pred_df.loc[pred_df['movement'] == 1]

	st.dataframe(pred_df_show['ticker'])

elif movement_to_show == 'Downward':

	pred_df_show = pred_df.loc[pred_df['movement'] == 0]

	st.dataframe(pred_df_show['ticker'])


# Show close price history
ticker = st.number_input('Enter a ticker to show the historical price and volume data', 
	min_value=0, 
	max_value=93, 
	format='%d')

# we use regular expression to select Close and Volume columns in data
data_cols = data.columns

r_close = re.compile("^C")
close_cols = filter(r_close.match, data_cols)
close = data.loc[ticker, close_cols].T
close_renamed = close.rename(lambda s: s.strip("C"))
close_renamed.index = close_renamed.index.astype('int64')

r_volume = re.compile("^V")
volume_cols = filter(r_volume.match, data_cols)
volume = data.loc[ticker, volume_cols].T
volume_renamed = volume.rename(lambda s: s.strip("V"))
volume_renamed.index = volume_renamed.index.astype('int64')

# Draw Close and Volume plots
st.write(
'''
### Price Historical Data

'''
)
st.line_chart(close_renamed)
st.write(
'''
### Volume Historical Data

'''
)
st.line_chart(volume_renamed)

st.write("""

**Disclaimer**: 
This content is for educational purposes only. The Information should not be construed as investment/trading advice and is not meant to be a solicitation or recommendation to buy, sell, or hold any securities.


\- Mohammad Tari

""")