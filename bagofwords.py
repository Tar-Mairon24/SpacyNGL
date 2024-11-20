from training_data import train_x, train_y
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

vectorizer = CountVectorizer(binary=True)
train_x_vectors = vectorizer.fit_transform(train_x)

clf_svm = svm.SVC(kernel='linear', probability=True)
clf_svm.fit(train_x_vectors, train_y)

test_x = vectorizer.transform(["pon los faros a maxima potencia"])

prediction_probabilities = clf_svm.predict_proba(test_x)

for i, probs in enumerate(prediction_probabilities):
    print(f"Prediction probabilities for '{test_x[i]}':")
    for label, prob in zip(clf_svm.classes_, probs):
        print(f"  {label}: {prob:.4f}")

prediction = clf_svm.predict(test_x)
print(f"Prediction: {prediction}")

