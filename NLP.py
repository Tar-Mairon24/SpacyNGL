import spacy
from sklearn import svm 
from training_data import train_x, train_y

nlp = spacy.load('es_core_news_lg')

docs = [nlp(text) for text in train_x]
print(docs[0].ents)

print("Pipeline components:", nlp.pipe_names)

print("Named entities:", docs[0].ents)

train_x_vectors = [x.vector for x in docs]

clf_svm = svm.SVC(kernel='linear', probability=True)
clf_svm.fit(train_x_vectors, train_y)

test_x = ["Prende la luz frontal"]
test_docs = [nlp(text) for text in test_x]
test_x_vectors = [x.vector for x in test_docs]

# Get the prediction probabilities
prediction_probabilities = clf_svm.predict_proba(test_x_vectors)

# Print the prediction probabilities
for i, probs in enumerate(prediction_probabilities):
    print(f"Prediction probabilities for '{test_x[i]}':")
    for label, prob in zip(clf_svm.classes_, probs):
        print(f"  {label}: {prob:.4f}")

prediction = clf_svm.predict(test_x_vectors)

# Print the prediction
print(f"Prediction: {prediction}")

# Print the class with the highest probability
for i, probs in enumerate(prediction_probabilities):
    max_prob_index = probs.argmax()
    print(f"Class with highest probability for '{test_x[i]}': {clf_svm.classes_[max_prob_index]} with probability {probs[max_prob_index]:.4f}")