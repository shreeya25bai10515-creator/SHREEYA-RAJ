from flask import Flask, request, jsonify
from sklearn.ensemble import IsolationForest
import numpy as np
import joblib

app = Flask(__name__)

# Load or train model
try:
    model = joblib.load('model.pkl')
except:
    model = IsolationForest(contamination=0.1, random_state=42)
    X_train = np.random.normal(100, 50, 1000).reshape(-1, 1)
    model.fit(X_train)
    joblib.dump(model, 'model.pkl')

@app.route('/detect-fraud', methods=['POST'])
def detect_fraud():
    data = request.json
    amount = data['amount']
    
    # Predict fraud
    prediction = model.predict([[amount]])
    fraud_score = model.decision_function([[amount]])[0]
    
    is_fraud = prediction[0] == -1
    
    return jsonify({
        'is_fraud': bool(is_fraud),
        'fraud_score': float(fraud_score),
        'amount': amount
    })

if __name__ == '__main__':
    app.run(port=5001, debug=True)
