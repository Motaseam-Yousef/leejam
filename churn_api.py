from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Define the relative paths for model, scaler, and target encoding mappings
MODEL_PATH = os.path.join('models', 'churn_best_xgb_model.pkl')
SCALER_PATH = os.path.join('models', 'scaler.pkl')
CITY_ENCODING_PATH = os.path.join('models', 'city_encoding.pkl')
REGION_ENCODING_PATH = os.path.join('models', 'region_encoding.pkl')

# Load the saved ensemble model, scaler, and target encodings
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
city_means = joblib.load(CITY_ENCODING_PATH)  # Target encoding for CITY
region_means = joblib.load(REGION_ENCODING_PATH)  # Target encoding for CENTER_REGION

# Define mapping dictionaries
mappings = {
    'PERSON_TYPE': {'PRIVATE': 0, 'CORPORATE': 1},
    'GENDER': {'M': 0, 'F': 1},
    'GX': {'No Showup': 0, 'GX Showup': 1},
    'PT': {'No Showup': 0, 'PT Showup': 1},
    'FT90_P': {'No Showup': 0, 'FT90 Showup': 1},
    'NO_PRGRAM': {'Go’s Solo': 0, 'At least one program': 1},
    'CENTER_REGION_CHANGE': {'False': 0, 'True': 1},
    'CITY_CHANGE': {'False': 0, 'True': 1}
}

@app.route('/churn_predict', methods=['POST'])
def predict():
    try:
        # Get input data
        input_data = request.json
        
        # Convert input data to DataFrame for processing
        df = pd.DataFrame([input_data])

        # Apply mappings using the defined dictionary
        df['PERSON_TYPE'] = df['PERSON_TYPE'].map(mappings['PERSON_TYPE'])
        df['GENDER'] = df['GENDER'].map(mappings['GENDER'])
        df['GX'] = df['GX'].map(mappings['GX'])
        df['PT'] = df['PT'].map(mappings['PT'])
        df['FT90_P'] = df['FT90_P'].map(mappings['FT90_P'])
        df['NO_PRGRAM'] = df['NO_PRGRAM'].map(mappings['NO_PRGRAM'])
        df['CENTER_REGION_CHANGE'] = df['CENTER_REGION_CHANGE'].map(mappings['CENTER_REGION_CHANGE'])
        df['CITY_CHANGE'] = df['CITY_CHANGE'].map(mappings['CITY_CHANGE'])

        # Apply the saved target encoding for CITY
        df['CITY'] = df['CITY'].map(city_means)

        # Apply the saved target encoding for CENTER_REGION directly
        df['CENTER_REGION'] = df['CENTER_REGION'].map(region_means)

        # Scale the data
        scaled_data = scaler.transform(df)

        # Predict using the model
        prediction = model.predict(scaled_data)

        # Get the probability of the prediction using predict_proba
        probabilities = model.predict_proba(scaled_data)

        # Probability of churn is the probability of class 0 (churn)
        churn_probability = probabilities[:, 0]  # Probability of churn (class 0)

        # Return both the prediction and the probability of churn
        return jsonify({
            'prediction': prediction.tolist(),  # 0 -> churn, 1 -> not churn
            'churn_probability': churn_probability.tolist()  # Probability of churn
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
