import streamlit as st
import pandas as pd
import joblib
import os

# Load the saved models, scalers, and target encodings
CHURN_MODEL_PATH = os.path.join('models', 'churn_best_xgb_model.pkl')
NBO_MODEL_PATH = os.path.join('models', 'nbo_xgb.pkl')
CHURN_SCALER_PATH = os.path.join('models', 'scaler.pkl')
NBO_SCALER_PATH = os.path.join('models', 'nbo_scaler.pkl')
CITY_ENCODING_PATH = os.path.join('models', 'city_encoding.pkl')
REGION_ENCODING_PATH = os.path.join('models', 'region_encoding.pkl')

churn_model = joblib.load(CHURN_MODEL_PATH)
nbo_model = joblib.load(NBO_MODEL_PATH)
churn_scaler = joblib.load(CHURN_SCALER_PATH)
nbo_scaler = joblib.load(NBO_SCALER_PATH)
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

# NBO Mapping
pkg_mapping = {
    5: 'MONTH_12_PKG',
    4: 'MONTH_9_PKG',
    3: 'MONTH_6_PKG',
    2: 'MONTH_3_PKG',
    1: 'MONTH_1_PKG',
    0: 'DAYS_1_PKG'
}

# Define the full feature set used by the churn model
churn_features = [
    'AGE', 'PERSON_TYPE', 'GENDER', 'GX', 'PT', 'FT90_P', 'NO_PRGRAM',
    'TOT_SUBS', 'REJOIN_CNT', 'RENEWAL_CNT', 'NEWSALE_CNT', 'FT_CENTER',
    'PRO_CENTER', 'PLUS_CENTER', 'XPRESS_CENTER', 'POPUP_CENTER',
    'HQ_CENTER', 'NO_OF_PRODUCTS', 'MONTH_12_PKG', 'MONTH_9_PKG',
    'MONTH_6_PKG', 'MONTH_3_PKG', 'MONTH_1_PKG', 'DAYS_1_PKG',
    'OUTAGE', 'SUBS_DAYS', 'OUTAGE_PERC', 'OUTAGE_TILLNOW',
    'CENTER_REGION_CHANGE', 'CITY_CHANGE', 'CITY', 'CENTER_REGION'
]

# Define the features used in NBO model training
nbo_features = [
    'AGE', 'PERSON_TYPE', 'GENDER', 'GX', 'PT', 'FT90_P', 'NO_PRGRAM',
    'TOT_SUBS', 'REJOIN_CNT', 'RENEWAL_CNT', 'NEWSALE_CNT', 'FT_CENTER',
    'PRO_CENTER', 'PLUS_CENTER', 'XPRESS_CENTER', 'POPUP_CENTER',
    'HQ_CENTER', 'NO_OF_PRODUCTS', 'OUTAGE', 'SUBS_DAYS', 'OUTAGE_PERC',
    'OUTAGE_TILLNOW', 'CENTER_REGION_CHANGE', 'CITY_CHANGE', 'CITY',
    'CENTER_REGION'
]

# Streamlit app configuration
st.set_page_config(page_title="LEEJAM Churn & NBO Predictor", page_icon="📊", layout="centered")

# Styled output display
st.markdown("""
    <style>
    .prediction-box {
        border: 2px solid #1a73e8;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0px;
        text-align: center;
        font-size: 24px;
        color: white;
        background-color: #1a73e8;
        font-weight: bold;
    }
    .probability-box {
        border: 2px solid #4caf50;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0px;
        text-align: center;
        font-size: 24px;
        color: white;
        background-color: #4caf50;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# App title and company name
st.title("📊 LEEJAM Churn & NBO Prediction")
st.write("Use this tool to predict customer churn and the next best offer based on selected attributes.")

# Input fields for categorical values
age = st.number_input("Age", min_value=18, max_value=100, value=35)
person_type = st.selectbox("Person Type", options=["PRIVATE", "CORPORATE"])
gender = st.selectbox("Gender", options=["M", "F"])
gx = st.selectbox("GX", options=["No Showup", "GX Showup"])
pt = st.selectbox("PT", options=["No Showup", "PT Showup"])
ft90_p = st.selectbox("FT90_P", options=["No Showup", "FT90 Showup"])
no_prgram = st.selectbox("NO_PRGRAM", options=["Go’s Solo", "At least one program"])
center_region = st.selectbox("Center Region", options=["CR", "WR", "ER", "AJ", "SH", "DU", "RAK"])
city = st.selectbox(
    "City",
    options=[
        "Riyadh", "Jeddah", "Dammam", "Mecca", "Madina", "Khobar", "Taif", "Jubail",
        "Ahsa", "Tabuk", "Buraidah", "Khamis Mushait", "Ajman", "Jizan", "Yanbu",
        "Hail", "Najran", "Skaka", "Arar", "Hafar Al Batin", "Sharjah", "Baha", "Abha",
        "Dubai", "Al Khobar", "Ras Al Khaimah", "Unaizah", "Dawadmi", "Unknown", "Majmaah",
        "Al Kharj City", "Muzahmiyah", "Jazan", "Ar Rass", "Sakaka"
    ]
)
center_region_change = st.selectbox("Center Region Change", options=["False", "True"])
city_change = st.selectbox("City Change", options=["False", "True"])

# Input fields for numerical values
tot_subs = st.number_input("Total Subscriptions", min_value=0, value=3)
rejoin_cnt = st.number_input("Rejoin Count", min_value=0, value=0)
renewal_cnt = st.number_input("Renewal Count", min_value=0, value=2)
newsale_cnt = st.number_input("New Sale Count", min_value=0, value=1)
ft_center = st.number_input("FT Center", min_value=0, value=3)
pro_center = st.number_input("Pro Center", min_value=0, value=0)
plus_center = st.number_input("Plus Center", min_value=0, value=0)
xpress_center = st.number_input("Xpress Center", min_value=0, value=0)
popup_center = st.number_input("Popup Center", min_value=0, value=0)
hq_center = st.number_input("HQ Center", min_value=0, value=0)
no_of_products = st.number_input("No. of Products", min_value=0, value=3)
month_12_pkg = st.number_input("12 Month Package", min_value=0, value=0)
month_9_pkg = st.number_input("9 Month Package", min_value=0, value=0)
month_6_pkg = st.number_input("6 Month Package", min_value=0, value=2)
month_3_pkg = st.number_input("3 Month Package", min_value=0, value=1)
month_1_pkg = st.number_input("1 Month Package", min_value=0, value=0)
days_1_pkg = st.number_input("Days 1 Package", min_value=0, value=0)
outage = st.number_input("Outage", min_value=0, value=4)
subs_days = st.number_input("Subscription Days", min_value=0, value=452)
outage_perc = st.number_input("Outage Percentage", min_value=0.0, value=0.027)
outage_tillnow = st.number_input("Outage Till Now", min_value=0, value=70233)

# Submit button
if st.button("Submit"):
    # Prepare the input data
    input_data = {
        "AGE": age,
        "PERSON_TYPE": person_type,
        "GENDER": gender,
        "GX": gx,
        "PT": pt,
        "FT90_P": ft90_p,
        "NO_PRGRAM": no_prgram,
        "TOT_SUBS": tot_subs,
        "REJOIN_CNT": rejoin_cnt,
        "RENEWAL_CNT": renewal_cnt,
        "NEWSALE_CNT": newsale_cnt,
        "FT_CENTER": ft_center,
        "PRO_CENTER": pro_center,
        "PLUS_CENTER": plus_center,
        "XPRESS_CENTER": xpress_center,
        "POPUP_CENTER": popup_center,
        "HQ_CENTER": hq_center,
        "NO_OF_PRODUCTS": no_of_products,
        "MONTH_12_PKG": month_12_pkg,
        "MONTH_9_PKG": month_9_pkg,
        "MONTH_6_PKG": month_6_pkg,
        "MONTH_3_PKG": month_3_pkg,
        "MONTH_1_PKG": month_1_pkg,
        "DAYS_1_PKG": days_1_pkg,
        "OUTAGE": outage,
        "SUBS_DAYS": subs_days,
        "OUTAGE_PERC": outage_perc,
        "OUTAGE_TILLNOW": outage_tillnow,
        "CENTER_REGION_CHANGE": center_region_change,
        "CITY_CHANGE": city_change,
        "CITY": city,
        "CENTER_REGION": center_region
    }

    # Convert to DataFrame for processing
    df = pd.DataFrame([input_data])

    # Apply mappings using the defined dictionary
    for col, mapping in mappings.items():
        df[col] = df[col].map(mapping)

    # Apply target encoding for CITY and CENTER_REGION
    df['CITY'] = df['CITY'].map(city_means)
    df['CENTER_REGION'] = df['CENTER_REGION'].map(region_means)

    # Ensure that the DataFrame has all the required churn features
    for feature in churn_features:
        if feature not in df:
            df[feature] = 0  # Assign 0 as default if any feature is missing

    # Scale the data for the churn prediction
    churn_scaled_data = churn_scaler.transform(df)

    # Predict churn using the churn model
    churn_prediction = churn_model.predict(churn_scaled_data)
    churn_probabilities = churn_model.predict_proba(churn_scaled_data)
    churn_probability = churn_probabilities[0, 0]  # Probability of churn

    # Display churn prediction
    churn_prediction_text = "Churn" if churn_prediction[0] == 0 else "Not Churn"
    st.markdown(f'<div class="prediction-box">Churn Prediction: {churn_prediction_text}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="probability-box">Probability of Churn: {churn_probability:.2f}</div>', unsafe_allow_html=True)

    # Filter the data to keep only the NBO features
    df_nbo = df[nbo_features]

    # Scale the filtered data for the next best offer (NBO) prediction
    nbo_scaled_data = nbo_scaler.transform(df_nbo)

    # Predict the next best offer using the NBO model
    nbo_prediction = nbo_model.predict(nbo_scaled_data)[0]

    # Map the prediction to the package name
    nbo_predicted_package = pkg_mapping[nbo_prediction]

    # Display NBO prediction
    st.markdown(f'<div class="prediction-box">Next Best Offer: {nbo_predicted_package}</div>', unsafe_allow_html=True)
    