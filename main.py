from fastapi import FastAPI

app = FastAPI()


#last update 2/11/2021 9:00 AM :https://www.xe.com/
@app.get("/rates")
def home():
    return {"USD":1,
            "EGP":15.63,
            "EUR":0.82,
            "GBP":0.72,
            "SAR":3.75,
            "AED":3.67,
            "KWD":0.30,
           
           }
