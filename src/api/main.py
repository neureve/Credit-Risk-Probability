from fastapi import FastAPI
from src.api.pydantic_models import CustomerFeatures, PredictionResponse
import mlflow.pyfunc
import pandas as pd

app = FastAPI()

# Load the best model from MLflow Registry
model_name = "credit-risk-model"  # Replace with your registered model name
model = mlflow.pyfunc.load_model(f"models:/{model_name}/Production")

@app.get("/")
def read_root():
    return {"message": "Credit Risk Prediction API is running!"}

@app.post("/predict", response_model=PredictionResponse)
def predict_risk(customer: CustomerFeatures):
    # Convert incoming Pydantic model to a DataFrame
    input_df = pd.DataFrame([customer.dict()])

    # Predict using the loaded MLflow model
    prediction = model.predict(input_df)

    return PredictionResponse(risk_probability=prediction[0])
