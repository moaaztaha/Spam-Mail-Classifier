# Spam Mail Classifier

## General 

- Get the email data
- Preprocess Pipeline for the emails 
  - HTML to plain text
  - Strip Headers, Lower case, Remove punctuation, replace URLs, replace numbers, stemming
  - Email to Word Counter 
  - Word Counter to Vector 
- Split data into train and test sets

### Easy Data: spam vs easy_ham

![image-20200201181655887](/media/kelwa/DEV/Code/DL/handson-ml2/SpamAssassin/imgs/image-20200201181655887.png)

- not bad using Logistic Regression on training set

  ![image-20200201181818215](/media/kelwa/DEV/Code/DL/handson-ml2/SpamAssassin/imgs/image-20200201181818215.png)

- on test set

### spam - hard_ham

- After trying several models (Logistic Regression, Random Forest, SVM) **Settled on Random Forest as it was the one was highest *recall score on the testset*** **98.98%** with **good Precision score 94.06%**

### All Ham + Spam 

- This made the data badly skewed as there were more ham emails than spam emails (2750 to 500)

  ![image-20200201185205698](/media/kelwa/DEV/Code/DL/handson-ml2/SpamAssassin/imgs/image-20200201185205698.png)

  - it's more clearer on the test set as the recall is very bad

    ![image-20200201185324265](/media/kelwa/DEV/Code/DL/handson-ml2/SpamAssassin/imgs/image-20200201185324265.png)

- Stratifying the data didn't help as the spam emails are too little

  ![image-20200201185559970](/media/kelwa/DEV/Code/DL/handson-ml2/SpamAssassin/imgs/image-20200201185559970.png)

  - testset resutls

    ​														 ![image-20200201185655194](/media/kelwa/DEV/Code/DL/handson-ml2/SpamAssassin/imgs/image-20200201185655194.png)

  ## Solution: Get more spam data

  ![image-20200201185925254](/media/kelwa/DEV/Code/DL/handson-ml2/SpamAssassin/imgs/image-20200201185925254.png)

  - Way better results 

    ![image-20200201190247786](/media/kelwa/DEV/Code/DL/handson-ml2/SpamAssassin/imgs/image-20200201190247786.png)

    - testset results 

    ![image-20200201190448308](/media/kelwa/DEV/Code/DL/handson-ml2/SpamAssassin/imgs/image-20200201190448308.png)