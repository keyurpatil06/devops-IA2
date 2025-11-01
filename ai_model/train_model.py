import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample banking queries and their labels
queries = [
    "Check account balance",
    "Forgot my PIN",
    "Open a new savings account",
    "Report lost credit card",
    "Change registered mobile number",
    "Activate my debit card",
    "Close my account",
    "Update address details",
    "Card not working at ATM",
    "Request account statement"
]

labels = [
    "Balance Inquiry",
    "PIN Issue",
    "Account Opening",
    "Card Issue",
    "Account Update",
    "Card Activation",
    "Account Closure",
    "Account Update",
    "Card Issue",
    "Statement Request"
]

# Vectorize the text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(queries)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Save model and vectorizer
joblib.dump(model, "ai_model/model.pkl")
joblib.dump(vectorizer, "ai_model/vectorizer.pkl")

print("Model trained and saved successfully!")
