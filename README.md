## **README for Churn Prediction and NBO Prediction API**

This project provides two prediction systems:

1. **Churn Prediction System** - Predicts customer churn based on various attributes.
2. **NBO (Next Best Offer) Prediction System** - Predicts the most active package for a customer.

Both systems include a Flask API for integration and a Streamlit UI for easy interaction.

---

### **Requirements**

Before running the APIs or the Streamlit UI, install the necessary dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

### **How to Run the APIs**

#### 1. **Run the Churn Prediction API**

- **Step 1**: Ensure the project folder is cloned/downloaded.
- **Step 2**: Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

- **Step 3**: Start the Flask API:

   ```bash
   python churn_api.py
   ```

- **Step 4**: Test the API using the `/churn_predict` endpoint. 

   - **Method**: POST
   - **URL**: `http://127.0.0.1:5000/churn_predict`
   - **Sample Input**:
     ```json
     {
     "AGE": 41.0,
     "PERSON_TYPE": "CORPORATE",
     "GENDER": "M",
     "GX": "No Showup",
     "PT": "GX Showup",
     "FT90_P": "No Showup",
     "NO_PRGRAM": "At least one program",
     "TOT_SUBS": 3.0,
     "REJOIN_CNT": 0.0,
     "RENEWAL_CNT": 2.0,
     "NEWSALE_CNT": 1.0,
     "FT_CENTER": 3.0,
     "PRO_CENTER": 0.0,
     "PLUS_CENTER": 0.0,
     "XPRESS_CENTER": 0.0,
     "POPUP_CENTER": 0.0,
     "HQ_CENTER": 0.0,
     "NO_OF_PRODUCTS": 3.0,
     "MONTH_12_PKG": 0.0,
     "MONTH_9_PKG": 0.0,
     "MONTH_6_PKG": 2.0,
     "MONTH_3_PKG": 1.0,
     "MONTH_1_PKG": 0.0,
     "DAYS_1_PKG": 0.0,
     "OUTAGE": 4.0,
     "SUBS_DAYS": 452.0,
     "OUTAGE_PERC": 0.027,
     "OUTAGE_TILLNOW": 70233.0,
     "CENTER_REGION_CHANGE": "False",
     "CITY_CHANGE": "False",
     "CITY": "Riyadh",
     "CENTER_REGION": "CR"
     }
     ```

   - **Sample Response**:
     ```json
     {
       "prediction": [0],  
       "churn_probability": [0.85] 
     }
     ```

#### 2. **Run the NBO Prediction API**

- **Step 1**: Follow the same steps to install the required dependencies as above.
- **Step 2**: Start the NBO Flask API:

   ```bash
   python nbo_api.py
   ```

- **Step 3**: Test the API using the `/predict_NBO` endpoint.

   - **Method**: POST
   - **URL**: `http://127.0.0.1:5000/predict_NBO`
   - **Sample Input**:
     ```json
     {
    "AGE": 41.0,
    "PERSON_TYPE": "CORPORATE",
    "GENDER": "M",
    "GX": "No Showup",
    "PT": "GX Showup",
    "FT90_P": "No Showup",
    "NO_PRGRAM": "At least one program",
    "TOT_SUBS": 3.0,
    "REJOIN_CNT": 0.0,
    "RENEWAL_CNT": 2.0,
    "NEWSALE_CNT": 1.0,
    "FT_CENTER": 3.0,
    "PRO_CENTER": 0.0,
    "PLUS_CENTER": 0.0,
    "XPRESS_CENTER": 0.0,
    "POPUP_CENTER": 0.0,
    "HQ_CENTER": 0.0,
    "NO_OF_PRODUCTS": 3.0,
    "OUTAGE": 4.0,
    "SUBS_DAYS": 452.0,
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
    "OUTAGE_PERC": 0.027,
    "OUTAGE_TILLNOW": 70233.0,
    "CENTER_REGION_CHANGE": "False",
    "CITY_CHANGE": "False",
    "CITY": "Riyadh",
    "CENTER_REGION": "CR"
     }
     ```

   - **Sample Response**:
     ```json
     {
       "predicted_package": "MONTH_6_PKG"
     }
     ```

---

### **How to Run the Streamlit UI**

#### 1. **Run Streamlit UI with Churn Prediction API**

- **Step 1**: Ensure the Churn API is running (`python churn_api.py`).
- **Step 2**: Run the Streamlit UI:

   ```bash
   streamlit run churn_ui.py
   ```

- **Step 3**: This will launch a web interface to input customer attributes and get churn predictions.

#### 2. **Run Streamlit UI and Model Together (No API for Both Churn & NBO)**

If you want to run both the Churn and NBO models directly within a single Streamlit app without using Flask:

```bash
streamlit run churn_ui.py
```

This combines both the models and UIs in one place, eliminating the need for separate APIs.

---

## Run overall

```
streamlit run main.py
```

### **Conclusion**

- **Churn Prediction** helps predict the likelihood of customers churning.
- **NBO Prediction** identifies the next best offer/package for a customer.