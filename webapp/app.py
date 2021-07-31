import streamlit as st
import pandas as pd
import re
import pickle

# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)

def prediction(ticker_to_predict):
    # Making predictions 
    prediction = classifier.predict(ticker_to_predict)
    return prediction


def main(): 

	st.write(
	'''
	# Will stock X's price go up or down the next day?


	Is there any pattern in the day to day movement of the stock prices? The app presents the
	prediction of the machine learning model at

	'''
	)
	st.markdown('[https://github.com/m-tari/stock_direction_predict_ml](https://github.com/m-tari/stock_direction_predict_ml)')
	st.write('The close price of 94 anonymized stocks are scaled to day 1 for 500 days.')


	data = pd.read_csv('./datasets/ohlc_data.csv')


	# Show close price history
	ticker = st.number_input('Enter a ticker to show the historical price and volume data (a number from 1-94)', 
		min_value=1, 
		max_value=94, 
		format='%d',
		key='ticker')

	# TODO: An input number for the number of days to display

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
	### Close Price Historical Data

	'''
	)
	st.line_chart(close_renamed)
	st.write(
	'''
	### Volume Historical Data

	'''
	)
	st.line_chart(volume_renamed)


	ticker_to_predict = st.number_input('Enter a ticker to show the movement prediction (a number from 1-94)', 
		min_value=1, 
		max_value=94, 
		format='%d',
		key='ticker_to_predict')

	# predict button
	if st.button('Predict the next day movment'):

		r_OC = re.compile("^[O, C]")
		OC_cols = filter(r_OC.match, data_cols)
		OC_df = data.loc[ticker_to_predict-1, OC_cols].iloc[880:899].to_frame().T

		st.write(OC_df)

		movement_to_show = prediction(OC_df)
		if movement_to_show == 1:
			st.write('Upward')
		elif movement_to_show == 0:
			st.write('Downward')

	st.write("""

	Disclaimer: 
	This content is for educational purposes only. The Information should not be construed as investment/trading advice and is not meant to be a solicitation or recommendation to buy, sell, or hold any securities.

	\- Mohammad Tari

	""")


if __name__=='__main__': 
    main()	