from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import make_scorer
import nltk
from sklearn.externals import joblib
from nltk.corpus import wordnet as wn
nltk.download('wordnet')
import pandas as pd 
import numpy as np


# read in data 
url = "https://raw.githubusercontent.com/josh-ashkinaze/Emotion-Colors/master/cleaned_data.json"
df = pd.read_json(url)

# Replace two labels so Wordnet can read the emotions
df['Emotion'] = df['Emotion'].replace('open-hearted', 'openhearted')
df['Emotion'] = df['Emotion'].replace('clear-headed', 'clearheaded')


# Define a semantic loss function 
def semantic_loss(truth, pred):
"""Creates a loss function based on semantic similarity."""
  error = 0 
  for i in range(0, len(pred)):
    truth_i = wn.synsets(truth[i])[0]
    pred_i = wn.synsets(truth[i])[0]
    error_i = truth_i.path_similarity(pred_i)
    error += error_i
  return error

# Grab our data
X = df['Color'].tolist()
y = df['Emotion'].tolist()

# Make scoring function
scorer = make_scorer(semantic_loss, greater_is_better=False)

# Create new knn model
knn = KNeighborsClassifier()

# Specify values to test 
param_grid = {'n_neighbors': np.arange(4, 25), 'weights':['uniform', 'distance']}

# Use gridsearch to test all values for n_neighbors
knn_gscv = GridSearchCV(knn, param_grid, cv=5, scoring=scorer)

# Fit model to data
knn_gscv.fit(X, y)

# Check out best params
print(knn_gscv.best_params_)

# Print best score
print(knn_gscv.best_score_)

# Save model
joblib.dump(knn_gscv.best_estimator_, 'filename.pkl')
