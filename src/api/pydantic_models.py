from pydantic import BaseModel

# Replace fields with your actual model input features
class CustomerFeatures(BaseModel):
    Recency: float
    Frequency: float
    Monetary: float

class PredictionResponse(BaseModel):
    risk_probability: float
