import joblib

def classify_query(query: str):
    model = joblib.load("ai_model/model.pkl")
    vectorizer = joblib.load("ai_model/vectorizer.pkl")

    X_new = vectorizer.transform([query])
    prediction = model.predict(X_new)[0]
    return prediction

if __name__ == "__main__":
    sample = "I lost my debit card"
    print(f"Query: {sample}")
    print("Predicted Category:", classify_query(sample))
