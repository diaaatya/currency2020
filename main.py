from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.

#last update 2/6/2021 1:00 PM
@app.get("/rates")
def home():
    return {"USD":1,
            "EGP":15.67,
            "EUR":0.83,
            "GBP":0.73,
            "SAR":3.75,
            "AED":3.67,
            "KWD":0.30,
           
           }
