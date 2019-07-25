import pandas as pd 
from ast import literal_eval

"""
Return a tidy json object with two columns:
a dominant color and an emotion. 
"""

def clean(df):
	df.dropna(inplace=True)
	df.drop_duplicates(inplace=True)
	
	# colors are cast to strings when saving as csv; 
	# recast colors back to original format 
	df['Color'] = [literal_eval(x) for x in df['color'].tolist()]
	
	df = df[['Color', 'Emotion']]
	df.reset_index(drop=True, inplace=True)
	return df

def main():
	df = pd.read_csv("emotions_images_colors.csv")
	cleaned = clean(df)

	# save to json to avoid tupples cast as strings
	cleaned.to_json('cleaned_data.json') 

main()
