from fastapi import FastAPI

app = FastAPI()


#last update 2/10/2021 8:33 AM
@app.get("/rates")
def home():
    return {"USD":1,
            "EGP":15.66,
            "EUR":0.83,
            "GBP":0.72,
            "SAR":3.75,
            "AED":3.67,
            "KWD":0.30,
           
           }
