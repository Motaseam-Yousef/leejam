import streamlit as st
import requests
import json

# Streamlit app configuration
st.set_page_config(page_title="LEEJAM Churn Predictor", page_icon="📊", layout="centered")

# App title and company name
st.title("📊 LEEJAM Churn Prediction")
st.write("Use this tool to predict customer churn based on selected attributes.")

# Blue theme style for inputs and buttons
st.markdown(
    """
    <style>
    .css-1offfwp {
        background-color: #1a73e8 !important;
        color: white !important;
        font-weight: bold !important;
    }
    .stButton>button {
        background-color: #1a73e8 !important;
        color: white !important;
        font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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

    # Send a POST request to the API
    try:
        response = requests.post("http://127.0.0.1:5000/churn_predict", json=input_data)
        if response.status_code == 200:
            result = response.json()
            churn_probability = result.get('churn_probability', ['N/A'])[0]
            churn_prediction = "Churn" if result['prediction'][0] == 0 else "Not Churn"

            # Display the results
            st.write(f"### Prediction: {churn_prediction}")
            st.write(f"### Probability of Churn: {churn_probability:.2f}")
        else:
            st.write("Error: Unable to connect to the API or invalid response.")
    except Exception as e:
        st.write(f"Error: {str(e)}")
