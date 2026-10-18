# Web App quizzes

Answers follow quiz IDs 17–18 in the repository's [English quiz data](../../../quiz-app/src/assets/translations/en.json).

## Quiz 17: Build a Web App — Pre-Lecture

1. What does ONNX stand for?  
   **Answer:** Open Neural Network Exchange.  
   It provides a shared model representation for interoperability between tools.
2. How is Flask defined by its creators?  
   **Answer:** micro-framework.  
   Flask provides the web application's core routing and request-handling facilities without requiring a large application structure.
3. What does Python's Pickle module do?  
   **Answer:** Serializes and De-serializes a Python Object.  
   Serialization saves an object's representation; deserialization reconstructs it. Load only trusted pickle artifacts.

## Quiz 18: Build a Web App — Post-Lecture

1. Which listed tool can host a pretrained model on the web using Python?  
   **Answer:** Flask.  
   A Flask route can validate submitted features, call a Python model, and return the prediction.
2. What does SaaS stand for?  
   **Answer:** Software as a Service.  
   Users access hosted software as a service instead of managing its entire installation themselves.
3. What does Scikit-learn's LabelEncoder do?  
   **Answer:** Encodes data alphabetically (the quiz's expected option).  
   More precisely, it maps target labels to integer IDs; string classes are sorted to establish that mapping. Save the encoder with the model and use `inverse_transform` to recover the original labels.
