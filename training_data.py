import pandas as pd

df = pd.read_csv('training_data.csv')

train_x = df['phrase'].tolist()
train_y = df['label'].tolist()

