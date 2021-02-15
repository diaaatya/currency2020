from fastapi import FastAPI

app = FastAPI()


#last update 2/15/2021 09:25 AM :https://www.xe.com/
@app.get("/rates")
def home():
    return {"USD":1,
            "EGP":15.57,
            "EUR":0.83,
            "GBP":0.72,
            "SAR":3.75,
            "AED":3.67,
            "KWD":0.30,
           
           }
