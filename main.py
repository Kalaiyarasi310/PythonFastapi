import uvicorn
from fastapi import FastAPI, status, Header, Request, Response
import models as mdl
from pydantic import BaseModel
import datetime
import logging

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}

@app.post("/ChatContent/", status_code = status.HTTP_200_OK)
async def ChatContent(sReq: mdl.SampleRequest):
    print("Request-------? ChatContent",sReq)
    return status.HTTP_200_OK


@app.get("/echo/{echostr}")
def read_item(echostr: str):
    return {"echostr": echostr}

class EchoPostReq(BaseModel):
    reqString: str

@app.post("/echopost")
def echopost(echostr: EchoPostReq):
    print("Request-------? echostr",echostr)
    return echostr

APP_NAME = "webhook-listener"
logger = logging.getLogger(APP_NAME)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_logging = logging.FileHandler(f"{APP_NAME}.log")
file_logging.setFormatter(formatter)
logger.addHandler(file_logging)

def do_something_with_the_event(data):
    logger.info("WebhookData received:")
    logger.info(f"Raw data: {data}")
    logger.info(f"Request Str: {data.reqString}")


@app.post("/webhook/",status_code=200)
async def webhook(
    webhook_input: EchoPostReq,
    request: Request,
    response: Response
):
    print ("webhook_input",webhook_input)
    #do_something_with_the_event(webhook_input)
    return {"result": "ok"}