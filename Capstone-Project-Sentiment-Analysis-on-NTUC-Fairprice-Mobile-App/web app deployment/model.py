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
    ('tvec', TfidfVectorizer(max_features = 2000, min_df=2, max_df=0.9, ngram_range=(1,1))),
    ('lr', LogisticRegression(solver='lbfgs', C=2.0, max_iter=100))
])

lr_tvec = pipe_lr_tvec.fit(X_train, y_train)

# MultinomialNB with TfidfVectorizer
pipe_nb_tvec = Pipeline([
    ('tvec', TfidfVectorizer(max_features=3000, min_df=1, max_df=0.9, ngram_range=(1,2))),
    ('nb', MultinomialNB(alpha=1.0))
])

nb_tvec = pipe_nb_tvec.fit(X_train, y_train)

# Voting Classifier
votingcl = VotingClassifier(estimators=[('lr_tvec', lr_tvec), ('nb_tvec', nb_tvec)],
                           voting='soft',    # soft voting predicts the class based on argmax of the sums of the predicted probabilities
                           weights = [1,2])  # higher weight for MultinomialNB as it has higher ROC AUC and precision
                                             # while accuracy and recall are same as logistic regression

votingcl.fit(X_train, y_train)

# Saving model as pickle file
pickle.dump(votingcl, open('model.pkl','wb'))
