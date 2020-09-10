# DSI Project 3: Reddit Post Classifier
------

## Problem Statement

I'm a data analyst working with with a mental health organisation to explore ways to better manage its patient support service. The patient support unit handles incoming text messages via social media messagers and chatbots from patients for follow up based on the patients' condition. 

In this project, the aim is to build a text classifier that can help to classify texts related to **depression** and **bipolar disorder**. These two conditions have some similarities in symptoms, but have their unique [differences](https://www.webmd.com/bipolar-disorder/bipolar-vs-depression) as well. By classifying the text messages by the conditions, they can be directed to the right specialists for appropriate care and treatment. This can be used to help mental health organisation's patient support unit improve patients' experience and productivity.

To build this text classifier, I will be using text posts from Reddit. **Reddit** is a website comprising user-generated content — including media and text-based posts — and discussions in a bulletin board system. The name "Reddit" is a play-on-words with the phrase "read it", i.e., "I read it on Reddit." As of 2018, there are approximately 330 million Reddit users, called "redditors". The site's content is divided into categories or communities known on-site as "subreddits", of which there are more than 138,000 active communities.

Given the nature of Reddit as a discussion forum, many patients and caretakers of patients with mental health conditions go to Reddit to get information and support in managing the condition, or simply sharing their personal experience and emotions in face of their condition. These posts can be used as the basis to build the text classifier.

In this project, I will:
* Extract posts from 2 subreddits using Reddit API: [r/depression](https://www.reddit.com/r/depression/) and [r/bipolar](https://www.reddit.com/r/bipolar/)
* Use **Natural Language Processing (NLP)** to build bag of words for each condition
* Apply several **Classification Models** to build **Text Classifers**, which will be evaluated.

An appropriate text classifier model should be one that have good accuracy and perform well classifying both text related to depression and bipolar disorder.


## Executive Summary

Among the various classifier models, **Support Vector Machine with TfidfVectorizer** performs marginally better than other models, with an accuracy of 81.88% and F1 score of 83.88%. 

However, it is noted that the **model perform much better in terms of sensitivity** of 88.52% (i.e. predicting actual positives/ depression cases correctly), and perform **not so well in terms of specificity** of 74.3% (predicting the actual negatives/ bipolar cases correctly).

A similar issue is noted for MultinomialNB model with TfidfVectorizer. While accuracy is 81.44% and F1 score is 83.03%, it has high sensitivity (85.25%) and low specificity (77.10%).

**Logistic Regression with TfidfVectorizer** may be a more balanced classification model. With a fairly comparable accuracy of 81.22% and F1 score of 82.3%, its performance in terms of sensitivity and specificity is more balanced (81.97% vs. 80.37%)


## Project Approach


### 1. Data Collection & Data Cleaning

The data used to build the text classifier were extracted from the Reddit API. Specifically, data were scrapped posts in 2 subreddits, namely:
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

|Model | Train Accuracy | Test Accuracy |Sensitivity | Specificity | Precision | F1 Score |
|:---  |:--- |:--- |:---  |:--- |:---  |:--- |
| Logistic Regression with CountVectorizer         | 0.7816 | 0.7860 | 0.8279 | 0.7383 | 0.7829 | 0.8048 |
| Logistic Regression with TfidfVectorizer         | 0.7955 | 0.8122 | 0.8197 | 0.8037 | 0.8264 | 0.8230 |
| MultinomialNB with CountVectorizer               | 0.7889 | 0.8057 | 0.8238 | 0.7850 | 0.8138 | 0.8187 |
| MultinomialNB with TfidfVectorizer               | 0.7926 | 0.8144 | 0.8525 | 0.7710 | 0.8093 | 0.8303 |
| SVM with CountVectorizer                         | 0.7620 | 0.7729 | 0.8361 | 0.7009 | 0.7612 | 0.7969 |
| SVM with TfidfVectorizer                         | 0.8027 | 0.8188 | 0.8852 | 0.7430 | 0.7970 | 0.8388 |


Among the various classifier models, **Support Vector Machine with TfidfVectorizer** performs marginally better, with an accuracy of 81.88% and F1 score of 83.88%. 

However, it is noted that: 

* the **model perform much better in terms of sensitivity** of 88.52% (i.e. predicting actual positives/ depression cases correctly), and 
* perform **not so well in terms of specificity** of 74.3% (predicting the actual negatives/ bipolar cases correctly).

**Logistic Regression with TfidfVectorizer** may be a more balanced classification model. With a fairly comparable accuracy of 81.22% and F1 score of 82.3%, its performance in terms of sensitivity and specificity is more balanced (81.97% vs. 80.37%). This means that the number of missclassification for each class (depression and bipolar) will be more similar. 


### 4. Misclassification Review

Among the False Positive cases (the model misclassify bipolar as depression) and False Negative cases (in which the model misclasify depression as bipolar), it is noted that:
* some of the posts were short/ generic (e.g. *'Except instead of powers I loose my mind...', I didn't wanted to talk with my brother because he and me like superheroes.*)
* some bipolar related posts were talking about depression and vice versa (e.g. this post was labelled as bipolar and misclassified as depression *'I’m feeling really depressed rn but I can’t tell anyone. I feel like I’m annoying tf out of everyone because I’m always sad and there’s nothing anybody can do or say to make me feel better. I try to smoke and just try to ignore it but now I’m just high af and even more depressed lol'*)
* and some patients seem to have both depression and bipolar, so the model was unable to classify properly



## Conclusions & Recommendations

### Conclusion

Among the various classifier models, **Support Vector Machine with TfidfVectorizer** performs marginally better, with an accuracy of 81.88% and F1 score of 83.88%. 

However, it is noted that: 

* the **model perform much better in terms of sensitivity** of 88.52% (i.e. predicting actual positives/ depression cases correctly), and 
* perform **not so well in terms of specificity** of 74.3% (predicting the actual negatives/ bipolar cases correctly).

A similar issue is noted for MultinomialNB model with TfidfVectorizer. While accuracy is 81.44% and F1 score is 83.03%, it has high sensitivity (85.25%) and low specificity (77.10%).

**Logistic Regression with TfidfVectorizer** may be a more balanced classification model. With a fairly comparable accuracy of 81.22% and F1 score of 82.3%, its performance in terms of sensitivity and specificity is more balanced (81.97% vs. 80.37%)


### Recommendations

From a patient support point of view, the **Logistic Regression classifier with TfidfVectorizer** should be deployed to ensure that there is a more balanced patient experience for both the depression patients and the bipolar patients. 

If the Support Vector Machine with TfidfVectorizer is used, there may be very good patient experience for the depression patients. However, patient experience for bipolar patients may be poor as more bipolar cases misclassified as depression cases due to the lower specificity of the model. It also means that the patient support chanelling efficiency will be lower as missclassified bipolar cases need to be manually channelled back to the depression unit. 

