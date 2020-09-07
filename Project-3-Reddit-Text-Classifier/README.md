# DSI Project 3: Reddit Post Classifier
------

## Problem Statement

**Reddit** is a website comprising user-generated content — including media and text-based posts — and discussions in a bulletin board system. The name "Reddit" is a play-on-words with the phrase "read it", i.e., "I read it on Reddit." As of 2018, there are approximately 330 million Reddit users, called "redditors". The site's content is divided into categories or communities known on-site as "subreddits", of which there are more than 138,000 active communities.

Given the nature of Reddit as a discussion forum, many patients and caretakers of patients with mental health conditions go to Reddit to get information and support in managing the condition, or simply sharing their personal experience and emotions in face of their condition.

This project focus on helping mental health organisations to better manage its patient support service when handling messages coming in via social media messagers or chatbots.

The two conditions chosen, **depression** and **bipolar disorder**, have some similarities in symptoms, but have their unique [differences](https://www.webmd.com/bipolar-disorder/bipolar-vs-depression) as well. It is also important to differentiate the conditions to direct to the right specialists for appropriate care and treatment.

* Extracting posts from 2 subreddits using Reddit API: [r/depression](https://www.reddit.com/r/depression/) and [r/bipolar](https://www.reddit.com/r/bipolar/)
* Use **Natural Language Processing (NLP)** to build bag of words for each condition
* Use **Classification Models** to build **Text Classifer** to help classify the text messages from social media/ messagers/ chatbots, so that they can be channel to the right team for follow up.

This can be used to help mental health organisations' patient support units improve patients' experience and productivity.


## Executive Summary





## Project Approach


### 1. Data Collection & Data Cleaning

The data used to build the text classifier were extracted from the Reddit API. Specificially, data were scrapped posts in 2 subreddits, namely:
1. [r/depression](https://www.reddit.com/r/depression/) and 
2. [r/bipolar](https://www.reddit.com/r/bipolar/)

The 'selftext', or the main text of the posts, were then used.

After removing duplicated posts and posts which do not have selftext (i.e. with media only), the dataset consists of:

|Subreddit | Number of posts |
|:---- | :----|
|Depression | 976 |
|Bipolar | 856 |


### 2. Preprocessing & EDA

The following pre-processing were performed on the data:
* Use regular expressions to remove non-word characters
* Convert words to lower case
* Use NLTK to remove stop words
* Remove words related to the subreddits such as 'depression' and 'bipolar' to prevent target leakage
* Removing frequently occurring words in both Depression and Bipolar subreddits e.g. 'feel', 'like', 'want' , etc
* Use NLTK Porter Stemmer to stem the words to their root form


### 3. Modelling

Various classification models such as Logistic Regression, Multinomial Naive Bayes, and Support Vector Machine,  were built using Pipeline and GridSearch, and were evaluated:

|Model | Accuracy | Sensitivity | Specificity | Precision | F1 Score |
|:---  |:--- |:---  |:--- |:---  |:--- |
| Logistic Regression with CountVectorizer| 0.7838 | 0.7910 | 0.7757 | 0.8008 | 0.7959 |
| Logistic Regression with TfidfVectorizer| 0.8188 | 0.8566 | 0.7757 | 0.8132 | 0.8343 |
| MultinomialNB with CountVectorizer      | 0.8057 | 0.8238 | 0.7850 | 0.8138 | 0.8187 |
| MultinomialNB with TfidfVectorizer      | 0.8144 | 0.8525 | 0.7710 | 0.8093 | 0.8303 |
| SVM with CountVectorizer                | 0.7642 | 0.8566 | 0.6589 | 



## Conclusions & Recommendations

