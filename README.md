# Fake Tweet Detector
## About
Fake Tweet Detector is an extension available for Chrome. Using machine learning, the extension can verify whether a tweet is real or fake, with an accuracy of 90%. This tool was designed to help discern between tweets published by bots or other bad-faith actors and tweets published by sincere authors. This tool requires no other installation of 3rd-party libraries or tools as it leverages an API. 

As the tool if not 100% accurate, there may be cases of false positives or false negatives.

## How To Run
To run this extension, first
- Download the _fake-tweet-detector-extension_ package
-  Type _chrome://extensions_ in the address bar
-  Select _Load unpacked_
-  Select the _fake-tweet-detector-extension_ package which contains a _background.js_ and _manifest.json_

## How To Use
On X/Twitter, highlight a tweet and rightclick. On the drop down menu, select _verify_. A notification will appear indicating that a tweet is predicated as real or fake.

## The Model
Many different models and vectorisation techniques were used and the best one selected. In this case, this was the K-Nearest Neighbour using TF-IDF vectorisation to achieve a F1 score of 0.93. The full process of discovery can be read through in the jupyter notebook contained in the _models_ package. The model was trained and tested on the MediaEval 2015 training and testing set containing 1000s of real and fake tweets. However these tweets are fairly dated and internet lexicon has developed even more since then. It could be hypothesied that using a recent dataset containing real and fake tweets from 2020-2024 could improve the accuracy even further in the deployment stage. 
