from fastapi import FastAPI

app = FastAPI()


#last update 2/19/2021 11:30 AM :https://www.xe.com/
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
