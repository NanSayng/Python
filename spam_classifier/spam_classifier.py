import pandas as pd
from sklearn.model_selection import train_test_split # to split data into train and test
from sklearn.feature_extraction.text import CountVectorizer # to convert msg to num
from sklearn.naive_bayes import MultinomialNB # to learn to classify spam
from sklearn.metrics import accuracy_score # to check model good job

# Step 1: Load the dataset
data = pd.read_csv('SMSSpamCollection', sep='\t', header=None, names=['label', 'message'])

# Step 2: Explore the data
print(data.head())
print(data['label'].value_counts())

# Step 3: Convert labels to numbers (spam=1, ham=0)
data['label_num'] = data.label.map({'ham':0, 'spam':1})

# Step 4: Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    data['message'], data['label_num'], test_size=0.2, random_state=42)

# Step 5: Convert text to numbers (vectorization)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Step 6: Train the model (Naive Bayes classifier)
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Step 7: Test the model and print accuracy
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Step 8: Test with your own messages
while True:
    msg = input("Enter a message to check (or 'quit' to stop): ")
    if msg.lower() == 'quit':
        break
    msg_vec = vectorizer.transform([msg])
    prediction = model.predict(msg_vec)
    print("Spam" if prediction[0] == 1 else "Not spam")
