# Thyroid Disease Detection using Machine Learning
## This is a project for Future Ready Talent's Microsoft Virtual Internship Program
Thyroid disease is a very common problem in India, more than one crore people are suffering with the disease every year. Thyroid disorder can speed up or slow down the metabolism of the body.

## Objective
* The main objective of this project is to predict if a person is having thyroid disease or not (no thyroid) with the help of Machine Learning.
* Classification algorithms such as SVM, Logistic Regression, Decision Tree and KNN Model have been trained on the thyroid dataset, UCI Machine Learning repository.
* After hyperparameter tuning Decision Tree model has performed well with better accuracy, precision and recall.
* Application has deployed on Heroku with the help of flask framework.

## Deployment Link
Heroku: https://thyroid-disease-detectioon.herokuapp.com/

### Technical Aspects
* Python 3.10
* Important Libraries: sklearn, pandas, numpy, matplotlib & seaborn
* Front-end: HTML, CSS 
* Back-end: Flask framework
* IDE: Jupyter Notebook, VSCode
* Database: Cassandra
* Deployment: Heroku

### How to run this app
follow these steps to run this app in vscode
* Create virtual environment - conda create -n myenv python=3.10
* Activate the environment - conda activate myenv
* Install the packages - pip install -r requirements.txt
* Run the app - python run app.py
Or you can simply follow the link below
* https://thyroid-disease-detectioon.herokuapp.com/

## Workflow
### Data Collection
* Thyroid Disease Data Set from UCI Machine Learning Repository.
* Link:https://archive.ics.uci.edu/ml/datasets/thyroid+disease
### Data Pre-processing
* Missing values handling by Simple imputation
* Categorical features handling by label encoding
* Feature scaling done by Standard Scalar method
* Drop unnecessary columns
### Model Creation and Evaluation
* Various classification algorithms like SVM, Decision Tree, Logistic Regression and KNN etc tested.
* All models performed well. However, Decision was chosen for the final model training and testing.
* Model performance evaluated based on accuracy, confusion matrix, f1_score

 ### Model Deployment
The final model is deployed on Heroku using Flask framework.
