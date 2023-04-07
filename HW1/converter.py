import pandas as pd

data_frame = pd.read_csv("Fortune500.txt", sep = '\s+', header = None)
data_frame.to_csv('Fortune500.csv', header = None)