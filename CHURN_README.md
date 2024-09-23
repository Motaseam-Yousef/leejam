## **README for Churn Prediction API and UI**

This project provides a customer churn prediction system. It includes a Flask API to predict churn based on various customer attributes and a Streamlit UI to easily interact with the model.

### **Project Structure**
```
- churn_api.py  # Flask application for the API
- churn_ui.py  # Simple Streamlit UI for sending requests to the API
- app.py  # Streamlit app with both UI and model integrated (no need for Flask)
- models/
    - churn_best_xgb_model.pkl  # Pretrained model
    - scaler.pkl  # Preprocessing scaler
    - city_encoding.pkl  # Encodings for city mapping
    - region_encoding.pkl  # Encodings for region mapping
- requirements.txt  # List of required packages
```

---

### **Requirements**

Before running the API or the Streamlit UI, ensure you have the necessary dependencies installed. Use the `requirements.txt` file to install all dependencies:

```bash
pip install -r requirements.txt
```

### **How to Run the Flask API**

1. **Clone the Project:**

   Download or clone the project folder to your local machine.

2. **Install the Required Packages:**

   Ensure you have Python installed, then install the dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask API:**

   Start the Flask API by running the following command in the project directory:

   ```bash
   python churn_api.py
   ```

   This will start the API at the default URL: `http://127.0.0.1:5000`

4. **Test the API Using cURL or Postman:**

   - **Endpoint**: `/churn_predict`
   - **Method**: `POST`
   - **URL**: `http://127.0.0.1:5000/churn_predict`

   ### **Sample Input**

   You can use the following sample JSON input to test the API:

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

   ### **Testing with Postman:**

   1. Open **Postman**.
   2. Create a new **POST** request.
   3. Enter the URL `http://127.0.0.1:5000/churn_predict`.
   4. In the **Body** tab, select **raw** and set it to **JSON** format.
   5. Paste the **sample input** in the body.
   6. Click **Send**.

   ### **Testing with cURL:**

   You can also test the API using `cURL` from the command line:

   ```bash
   curl -X POST http://127.0.0.1:5000/churn_predict \
   -H "Content-Type: application/json" \
   -d '{INPUT_DATA}'
   ```

5. **Response Example:**

   The API will return the prediction and the probability of churn.

   Example response:
   ```json
   {
     "prediction": [0],  # 0 -> churn, 1 -> not churn
     "churn_probability": [0.85]  # Probability of churn (85%)
   }
   ```

---

### **How to Run the Streamlit UI**

1. **Run the Streamlit UI with API**:

   You can use a simple **Streamlit UI** to interact with the Flask API. First, ensure the Flask API is running (`python churn_api.py`), then run the Streamlit UI:

   ```bash
   streamlit run churn_ui.py
   ```

   This will open a web interface where you can input the customer attributes and get a churn prediction by calling the Flask API.

---

### **How to Run the Streamlit UI and Model Together (No API)**

If you'd like to run the **Streamlit UI** and prediction model directly within the same file (without the need for Flask API), run the following command:

```bash
streamlit run app.py
```

This combines the model and the UI in one place, eliminating the need for the API.

---

### **Conclusion:**

- The project offers a flexible approach to predicting customer churn.
- You can use the **Flask API** for integration with external services or use the **Streamlit UI** for a more user-friendly approach.
- For the easiest setup, run the combined `app.py` with Streamlit.