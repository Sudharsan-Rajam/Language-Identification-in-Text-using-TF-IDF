import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Split the data into 70:30 ratio for train and test
train, test = train_test_split(pr.df_data, test_size=0.3, random_state=42, shuffle=True)
train_df = pd.DataFrame(train)
test_df  = pd.DataFrame(test)

# fit the training data to the model
x=train_df.iloc[:,0]
y=train_df.iloc[:,1]
vectorizer = TfidfVectorizer(ngram_range = (1,3), analyzer = 'char')
pipe_line_lr  = Pipeline([('Vectorizer', vectorizer),('clf',LogisticRegression())]) 
pipe_line_rfc  = Pipeline([('Vectorizer', vectorizer),('clf',RandomForestClassifier())]) 
pipe_line_rfc.fit(x,y)
pipe_line_lr.fit(x,y)

# Prediction 
y_predicted_lr = pipe_line_lr.predict(test_df.iloc[:,0])
crosstab_result_lr = pd.crosstab(y_predicted_lr,test_df.iloc[:,1])
y_predicted_rf = pipe_line_rf.predict(test_df.iloc[:,0])
crosstab_result_rf = pd.crosstab(y_predicted_rf_lr,test_df.iloc[:,1])

print(crosstab_result_lr)
print(crosstab_result_rf)

# accuracy
Accuracy_lr = (accuracy_score(test_df.iloc[:,1],y_predicted_lr))*100
Accuracy_rf = (accuracy_score(test_df.iloc[:,1],y_predicted_rf))*100
