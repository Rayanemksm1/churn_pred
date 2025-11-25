import pandas as pd
import joblib

# Charger le modèle
model = joblib.load("model_churn.pkl")

def predire_churn(client_data: dict):
    """
    client_data = {
        "age": ...,
        "gender": ...,
        "country": ...,
        "subscription_length": ...,
        "monthly_fee": ...,
        "nb_support_tickets": ...,
        "last_login_days": ...,
        "contract_type": ...,
        "is_active": ...
    }
    """
    
    df = pd.DataFrame([client_data])
    
    # Prédiction
    classe = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]   # probabilité que churn=1
    
    return classe, proba
