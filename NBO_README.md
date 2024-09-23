# NBO Prediction API

This Flask API predicts the most active package for a customer based on various features. It loads a pre-trained XGBoost model, applies necessary mappings, encodes features, and scales them before making a prediction.

## Requirements

Install the dependencies listed in the `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Endpoint

- **POST** `/predict_NBO`
  - This endpoint accepts JSON input, processes it using the pre-trained model, and returns the predicted package name.

## Run code 
```
python nbo_api.py
```

## Input Sample

Here’s an example of the JSON input to be sent to the `/predict_NBO` endpoint:

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
}
```

## Testing the API

### Using Postman

1. Open Postman.
2. Create a new POST request.
3. Set the URL to: `http://127.0.0.1:5000/predict_NBO`
4. In the Body tab, select `raw` and set the content type to `JSON`.
5. Paste the sample JSON input in the body and send the request.

### Using cURL

You can also test the API using `curl` from the command line:

```bash
curl -X POST http://127.0.0.1:5000/predict_NBO \
-H "Content-Type: application/json" \
-d '{INPUT_DATA}'
```

This will return the predicted package in the following format:

```json
{
    "predicted_package": "MONTH_6_PKG"
}
```