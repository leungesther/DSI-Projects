# import libraries
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import VotingClassifier
import pickle

# read data
reviews_for_modelling = pd.read_csv('reviews_for_modelling.csv')

df = reviews_for_modelling.copy()
X = df['review_lem']
y = df['neg_review']

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)

# Logistic Regression with TfidfVectorizer
pipe_lr_tvec = Pipeline([
    ('tvec', TfidfVectorizer()),
    ('lr', LogisticRegression(solver='lbfgs'))
])

pipe_lr_tvec_params = {
    'tvec__max_features': [2000],   # tried [2000, 3000, 4000, 5000]
    'tvec__min_df': [2],            # tried [1, 2]
    'tvec__max_df': [0.9],          # tried [0.9, 0.95, 1.0]
    'tvec__ngram_range': [(1, 1)],  # tried [(1, 1), (1,2), (2,2)]
    'lr__C': [2.0],                 # tried [1.0, 2.0]
    'lr__max_iter': [100]           # tried [100, 200]
}

gs_lr_tvec = GridSearchCV(pipe_lr_tvec, param_grid = pipe_lr_tvec_params, cv=5)

gs_lr_tvec.fit(X_train, y_train)

# MultinomialNB with TfidfVectorizer
pipe_nb_tvec = Pipeline([
    ('tvec', TfidfVectorizer()),
    ('nb', MultinomialNB())
])

pipe_nb_tvec_params = {
    'tvec__max_features': [3000],  # tried [2000, 3000, 4000, 5000]
    'tvec__min_df': [1],           # tried [1, 2]
    'tvec__max_df': [0.9],         # tried [0.9, 0.95, 1.0]
    'tvec__ngram_range': [(1,2)],  # tried [(1, 1), (1,2), (2,2)]
    'nb__alpha': [1.0]             # tried [1.0, 1e-1, 1e-2]
}

gs_nb_tvec = GridSearchCV(pipe_nb_tvec, param_grid = pipe_nb_tvec_params, cv=5)

gs_nb_tvec.fit(X_train, y_train)

# Voting Classifier
votingcl = VotingClassifier(estimators=[('lr_tvec', gs_lr_tvec), ('nb_tvec', gs_nb_tvec)],
                           voting='soft',    # soft voting predicts the class based on argmax of the sums of the predicted probabilities
                           weights = [1,2])  # higher weight for MultinomialNB as it has higher ROC AUC and precision
                                             # while accuracy and recall are same as logistic regression

votingcl.fit(X_train, y_train)

# Saving model as pickle file
pickle.dump(votingcl, open('model.pkl','wb'))
