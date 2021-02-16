from fastapi import FastAPI

app = FastAPI()


#last update 2/16/2021 09:00 AM :https://www.xe.com/
@app.get("/rates")
def home():
    return {"USD":1,
            "EGP":15.60,
            "EUR":0.82,
            "GBP":0.72,
            "SAR":3.75,
            "AED":3.67,
            "KWD":0.30,
           
           }
