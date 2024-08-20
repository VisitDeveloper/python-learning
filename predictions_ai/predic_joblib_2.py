import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
import joblib

# music_data = pd.read_csv('music.csv')
# X = music_data.drop(columns=['genre'])
# y = music_data['genre']


# model = DecisionTreeClassifier()
# model.fit(X , y)

# فراخوانی مدل آموزش دیده 
model = joblib.load('music-recomender.joblib')
predictions = model.predict([[21, 1]])
predictions
