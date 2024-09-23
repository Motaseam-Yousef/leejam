from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the saved model and scaler
MODEL_PATH = os.path.join('models', 'nbo_xgb.pkl')
SCALER_PATH = os.path.join('models', 'nbo_scaler.pkl')
xgb_model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Load city and region encodings
CITY_ENCODING_PATH = os.path.join('models', 'city_encoding.pkl')
REGION_ENCODING_PATH = os.path.join('models', 'region_encoding.pkl')
city_means = joblib.load(CITY_ENCODING_PATH)
region_means = joblib.load(REGION_ENCODING_PATH)

# Define mappings
pkg_mapping = {
    5: 'MONTH_12_PKG',
    4: 'MONTH_9_PKG',
    3: 'MONTH_6_PKG',
    2: 'MONTH_3_PKG',
    1: 'MONTH_1_PKG',
    0: 'DAYS_1_PKG'
}

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

@app.route('/predict_NBO', methods=['POST'])
def predict():
    # Extract data from request
    data = request.json
    df = pd.DataFrame([data])

    # Apply mappings to the input data
    for col, mapping in mappings.items():
        df[col] = df[col].map(mapping)
    
    # Apply the saved target encoding for CITY and CENTER_REGION
    df['CITY'] = df['CITY'].map(city_means)
    df['CENTER_REGION'] = df['CENTER_REGION'].map(region_means)

    # Select only the required features
    features = [
        'AGE', 'PERSON_TYPE', 'GENDER', 'GX', 'PT', 'FT90_P', 'NO_PRGRAM',
        'TOT_SUBS', 'REJOIN_CNT', 'RENEWAL_CNT', 'NEWSALE_CNT', 'FT_CENTER',
        'PRO_CENTER', 'PLUS_CENTER', 'XPRESS_CENTER', 'POPUP_CENTER',
        'HQ_CENTER', 'NO_OF_PRODUCTS', 'OUTAGE', 'SUBS_DAYS', 'OUTAGE_PERC',
        'OUTAGE_TILLNOW', 'CENTER_REGION_CHANGE', 'CITY_CHANGE', 'CITY',
        'CENTER_REGION'
    ]
    df_features = df[features]

    # Scale the features
    df_scaled = scaler.transform(df_features)

    # Make prediction using the model
    prediction = xgb_model.predict(df_scaled)[0]

    # Map prediction back to the package name
    predicted_package = pkg_mapping[prediction]

    # Return the prediction as JSON
    return jsonify({'predicted_package': predicted_package})

if __name__ == '__main__':
    app.run(debug=True)
