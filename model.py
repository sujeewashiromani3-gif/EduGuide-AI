from sklearn.tree import DecisionTreeClassifier

# Training data: [math, science, english, attendance]
X = [
    [90, 85, 88, 95],
    [80, 78, 82, 85],
    [70, 72, 68, 75],
    [60, 65, 62, 70],
    [50, 55, 52, 60],
    [40, 45, 42, 55],
    [30, 35, 32, 50],
]

# Labels
y = [
    "High Performer",
    "Good",
    "Average",
    "Below Average",
    "Needs Improvement",
    "At Risk",
    "Critical"
]

# Train model once
model = DecisionTreeClassifier()
model.fit(X, y)

# Prediction function used by Flask app
def predict_student(math, science, english, attendance):
    return model.predict([[math, science, english, attendance]])[0]