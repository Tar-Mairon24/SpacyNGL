import joblib

# Load the saved model and vectorizer
model = joblib.load('logistic_regression_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

def predict_intent(query, threshold=0.6):
    query_tfidf = vectorizer.transform([query])  # Transform input query
    probabilities = model.predict_proba(query_tfidf)
    max_prob = max(probabilities[0])
    if max_prob >= threshold:
        return model.predict(query_tfidf)[0]
    else:
        return "fallback"

# Example usage
new_query = "Prende faros en alto"
print(f"Predicted Intent: {predict_intent(new_query)}")
