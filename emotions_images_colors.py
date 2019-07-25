from colorthief import ColorThief
from urllib.request import urlopen
import io
import pandas as pd
import numpy as np

def get_dominant_color(url):
  """Given an image in url format, eturn the dominant color."""
  try:
    img = urlopen(url)
    f = io.BytesIO(img.read())
    color_thief = ColorThief(f)
    color = color_thief.get_color(quality=1)
    return color
  except:
    return np.NaN 

def main():
  df = pd.read_csv("emotions_images.csv")
  urls = df['Url'].tolist()
  colors = [get_dominant_color(url) for url in urls]
  df['color'] = colors
  df.to_csv("emotions_images_colors.csv")
  
main()
